import enum
import random
import struct
import time
import ctypes
from sys import platform

import libusb_package
import usb.core
import usb.util
import usb.backend.libusb1
from time import localtime, strftime
from datetime import datetime
from collections import deque
from PySide6.QtCore import Qt, QTimer, Slot

sensor_name = {0xBD: "Датчик шума", 0xBC: "Термопара", 0xBA: "Датчик тока",
               0xBE: "Датчик пульса", 0xBB: "Датчик света", 0xBF: "Датчик ультрафиолета",
               0xB1: "Датчик давления", 0xB2: "Датчик влажности", 0xB3: "Датчик температуры"}

sensor_unit = {0xBD: "dB", 0xBC: "C", 0xBA: "A",
               0xBE: "", 0xBB: "Lux", 0xBF: "P/(w*w)",
               0xB1: "Pa", 0xB2: "%", 0xB3: "C"}
index_to_cmd = {0: 0x12, 1: 0x13, 2: 0x14, 3: 0x15, 4: 0x16, 5: 0x17, 6: 0x18, 7: 0x19, 8: 0x24, 9: 0x25, 10: 0x26,
                11: 0x27, 12: 0x28}


class ReportId(enum.Enum):
    REPORT_OUT = 0x21
    REPORT_IN_1 = 0x11
    REPORT_IN_2 = 0x12
    REPORT_IN_3 = 0x13


class UsbCmd(enum.Enum):
    SENSOR_NUM = 0x11
    BUS_1 = 0x12
    BUS_2 = 0x13
    BUS_3 = 0x14
    BUS_4 = 0x15
    BUS_5 = 0x16
    BUS_6 = 0x17
    BUS_7 = 0x18
    BUS_8 = 0x19
    START = 0x20
    STOP = 0x21
    START_CONDITION = 0x22
    SET_DATE = 0x23


class SensorSd:
    def __init__(self, index: int):
        self.id: int = index
        self.available: bool = False
        self.who_am_i: int | None = 0
        self.name: str | None = None
        self.x: list = []
        self.y: list = []

    def parse_first_sd_data(self, data):
        id_to_data_idx = 5*self.id + 9
        wai = data[id_to_data_idx]
        if wai != 0:
            self.available = True
            self.who_am_i = wai
            self.name = sensor_name[self.who_am_i]
            self.x = []
            self.y = []
            datac = (ctypes.c_char * 4)()
            datac[0] = data[id_to_data_idx + 1]
            datac[1] = data[id_to_data_idx + 2]
            datac[2] = data[id_to_data_idx + 3]
            datac[3] = data[id_to_data_idx + 4]
            data_f = struct.unpack('f', bytes(datac))
            data_v = round(data_f[0], 2)
            self.y.append(data_v)
            self.x.append(0)

    def parse_sd_data(self, data):
        id_to_data_idx = 5 * self.id + 9
        wai = data[id_to_data_idx]
        if wai != 0:
            datac = (ctypes.c_char * 4)()
            datac[0] = data[id_to_data_idx + 1]
            datac[1] = data[id_to_data_idx + 2]
            datac[2] = data[id_to_data_idx + 3]
            datac[3] = data[id_to_data_idx + 4]
            data_f = struct.unpack('f', bytes(datac))
            data_v = round(data_f[0], 2)
            self.y.append(data_v)
            self.x.append(self.x[-1]+1)


class Sensor:
    def __init__(self, index: int, name: str = "Не подключен", connected: bool = False):
        self.id: int = index
        self.connected: bool = connected
        self.who_am_i: int = 0
        self.name: str | None = name
        self.frequency: int = 1
        self.running: bool = False
        self.unit: str = ""
        self.x: list = list(range(100))
        self.y: list = [0 for _ in range(100)]


class DlmmUSB:
    def __init__(self, pid: int, vid: int):
        self.pid = pid
        self.vid = vid
        self.device = None
        self.start_condition = 0
        self.first_connection: bool = True
        self.sd_checked: bool = False
        self.sd_last_data: datetime | None = None
        self.sd_empty: bool = True
        self.sd_first_block = 2
        self.sd_last_block = 2
        self.sd_last_data_size = 0
        self.data_downloaded: bool = False

    def check_device(self) -> bool:
        try:
            dev = None
            # dev = usb.core.find(idVendor=self.vid, idProduct=self.pid)
            # print(dev)
            # dev.set_configuration()
            if platform == "linux" or platform == "linux2":
                # print(f"LINUX {platform}")
                dev = usb.core.find(idVendor=self.vid, idProduct=self.pid)

                # dev.set_configuration()
            elif platform == "win32":
                # print(f"WINDOWS {platform}")
                dev = libusb_package.find(idVendor=self.vid, idProduct=self.pid)

            # print(dev)
            # dev = usb.core.find(idVendor=self.vid, idProduct=self.pid)
            # print(dev)
            if dev is self.device and dev is not None:
                return True
            if not dev:
                self.device = None
                return False
            if self.device is None:
                self.first_connection = True
                # print(type(dev))
                self.device = dev
                # print(self.device)
                # print(self.device)
                '''reattach = False
                if self.device.is_kernel_driver_active(0):
                    reattach = True
                    self.device.detach_kernel_driver(0)'''
                if platform == "linux" or platform == "linux2":
                    reattach = False
                    if self.device.is_kernel_driver_active(0):
                        reattach = True
                        self.device.detach_kernel_driver(0)

                cfg = usb.util.find_descriptor(self.device, bConfigurationValue=1)
                cfg.set()
                # time.sleep(1)
                # self.set_date()
                return True
        except ValueError as e:
            print(f'check_device Timeout error {e}')
            self.device = None
            return False
        except usb.core.USBError as e:
            print(f'check_device USB error {e}')
            if "Resource busy" not in str(e):
                self.device = None
            return False

    def get_start_condition(self) -> None:

        if self.device is None:
            self.check_device()

        try:
            self.device.write(0x1, [ReportId.REPORT_OUT, UsbCmd.START_CONDITION], 1000)
            ret = self.device.read(0x81, 64, 1000)
            self.start_condition = ret[2]
        except usb.core.USBTimeoutError:
            print('Write Timeout error')
        except usb.core.USBError as e:
            self.device = None
            print(f"USB ERR get_start_condition {e}")

    def set_start_condition(self, cond: int = 0x21):
        if self.device is None:
            self.check_device()

        try:
            # print('set start cond')
            self.device.write(0x1, [0x21, cond], 1000)
            ret = self.device.read(0x81, 64, 1000)
            # print(f'start cond {ret}')
            self.start_condition = ret[2]
        except usb.core.USBTimeoutError as e:
            print(f'set_start_condition Timeout error {e}')
        except usb.core.USBError as e:
            self.device = None
            print(f'set_start_condition usb error {e}')
        except AttributeError as e:
            print(f"set_start_condition attribute error {e}")

    def get_available_sensors(self, sensors: list[Sensor]):
        if self.device is None:
            self.check_device()
        if self.device is None:
            for s in sensors:
                s.connected = False

        try:
            # self.device.write(0x1, [ReportId.REPORT_OUT, UsbCmd.SENSOR_NUM], 1000)
            self.device.write(0x1, [0x21, 0x11], 1000)
            ret = self.device.read(0x81, 64, 1000)
            # print(f'sensors {ret}')
            if ret[1] == 17:
                for i, s in enumerate(sensors):
                    if ret[i + 2] != 0:
                        s.connected = True
                        s.who_am_i = ret[i + 2]
                        s.name = sensor_name[s.who_am_i]
                        s.unit = sensor_unit[s.who_am_i]
                    else:
                        s.connected = False
                        s.who_am_i = 0
                        s.name = None
                    # print(i, s.connected)
        except usb.core.USBTimeoutError:
            print("get_available_sensors Timeout error")
        except usb.core.USBError as e:
            self.device = None
            print(f"get_available_sensors usb error {e}")
        except AttributeError:
            pass

    def get_data_from_sensor(self, sensor: Sensor) -> float:
        if self.device is None:
            self.check_device()
        if self.device is not None and sensor.connected:
            # print('sens get data')
            try:
                if self.start_condition == 0:
                    self.set_start_condition(0x20)
                # print(index_to_cmd[sensor.id])
                self.device.write(0x1, [0x21, index_to_cmd[sensor.id]], 1000)
                ret = self.device.read(0x81, 64, 1000)
                data = (ctypes.c_char * 4)()
                data[0] = ret[4]
                data[1] = ret[5]
                data[2] = ret[6]
                data[3] = ret[7]
                data_f = struct.unpack('f', bytes(data))
                data_v = round(data_f[0], 2)
                if ret[2] == 0xBE and int(data_v) == -999:
                    data_v = 0.0
                # print(ret)
                return data_v
            except usb.core.USBTimeoutError:
                print("get_data_from_sensor Timeout error")
                return 0.0
            except usb.core.USBError as e:
                print(f"USB ERR get data {e}")
                self.device = None
                return 0.0
            except AttributeError:
                print("ATTRIBUTE ERR get data")
                return 0.0

    def set_date(self):
        date = localtime()
        yy = date.tm_year % 100
        mm = date.tm_mon
        dd = date.tm_mday
        HH = date.tm_hour
        MM = date.tm_min
        SS = date.tm_sec
        DOW = date.tm_wday
        # print(yy, mm, dd, HH, MM, SS, DOW)
        try:
            self.device.write(0x1, [0x22, 0x23, yy, mm, dd, HH, MM, SS, DOW], 1000)
            ret = self.device.read(0x81, 64, 1000)
            # print(ret)
        except usb.core.USBTimeoutError as e:
            print(f"set_date Timeout error {e}")
        except usb.core.USBError as e:
            print(f"USB ERR set date {e}")
        except AttributeError:
            print("ATTRIBUTE ERR set date")

    def get_sd_info(self):
        try:
            self.device.write(0x1, [0x21, 0x27], 1000)
            ret = self.device.read(0x81, 64, 1000)
            self.sd_checked = True
            if ret[3] == 0 or ret[4] == 0 or ret[5] == 0:
                self.sd_last_data = None
            else:
                self.sd_last_data = datetime(year=ret[3]+2000, month=ret[4], day=ret[5])
            if ret[2] == 1:
                self.sd_empty = True
            else:
                self.sd_empty = False
            data = (ctypes.c_char * 4)()
            data[0] = ret[6]
            data[1] = ret[7]
            data[2] = ret[8]
            data[3] = ret[9]
            data_f = struct.unpack('I', bytes(data))
            self.sd_first_block = data_f[0]
            data[0] = ret[10]
            data[1] = ret[11]
            data[2] = ret[12]
            data[3] = ret[13]
            data_f = struct.unpack('I', bytes(data))
            self.sd_last_block = data_f[0]
            self.sd_last_data_size = round((self.sd_last_block - self.sd_first_block)*496/1024, 2)
            print(self.sd_last_data_size)
            print(ret)
        except usb.core.USBTimeoutError as e:
            print(f"get_sd_info Timeout error {e}")
        except usb.core.USBError as e:
            print(f"USB ERR get_sd_info {e}")
        except AttributeError:
            print("ATTRIBUTE ERR get_sd_info")

    def get_sd_data(self, sensors: list[SensorSd]):
        try:
            self.device.write(0x1, [0x21, 0x28], 1000)
            ret = self.device.read(0x81, 64, 1000)
            for i in sensors:
                i.parse_first_sd_data(ret)
            while ret[1] != 1:
                self.device.write(0x1, [0x21, 0x28], 2000)
                ret = self.device.read(0x81, 64, 1000)
                for i in sensors:
                    i.parse_sd_data(ret)
            print(sensors[0].y)
            self.data_downloaded = True
        except usb.core.USBTimeoutError as e:
            print(f"set_date Timeout error {e}")
        except usb.core.USBError as e:
            print(f"USB ERR set date {e}")
        except AttributeError:
            print("ATTRIBUTE ERR set date")

class UsbCommunication:
    def __init__(self):
        pass

    @staticmethod
    def check_connections() -> tuple:
        r1, r2, r3 = random.sample(range(0, 7), 3)
        # print(r1, r2, r3)
        return r1, r2, r3
