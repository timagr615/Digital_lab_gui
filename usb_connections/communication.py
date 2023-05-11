import enum
import random
import struct
import time
import ctypes
import usb.core
import usb.util
from time import localtime, strftime
from collections import deque
from PySide6.QtCore import Qt, QTimer, Slot

sensor_name = {0xBD: "Датчик шума", 0xBC: "Термопара", 0xBA: "Датчик тока",
               0xBE: "Датчик пульса", 0xBB: "Мультидатчик", 0xBF: "Датчик ультрафиолета"}
index_to_cmd = {0: 0x12, 1: 0x13, 2: 0x14, 3: 0x15, 4: 0x16, 5: 0x17, 6: 0x18, 7: 0x19}


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


class Sensor:
    def __init__(self, index: int, name: str = "Не подключен", connected: bool = False):
        self.id: int = index
        self.connected: bool = connected
        self.who_am_i: int = 0
        self.name: str | None = name
        self.frequency: int = 1
        self.running: bool = False
        self.x: list = list(range(100))
        self.y: list = [0 for _ in range(100)]


class DlmmUSB:
    def __init__(self, pid: int, vid: int):
        self.pid = pid
        self.vid = vid
        self.device = None
        self.start_condition = 0

    def check_device(self) -> bool:
        try:
            dev = usb.core.find(idVendor=self.vid, idProduct=self.pid)
            # print(dev)
            if dev is self.device and dev is not None:
                return True
            if not dev:
                self.device = None
                return False
            if self.device is None:

                self.device = dev

                # print(self.device)
                reattach = False
                if self.device.is_kernel_driver_active(0):
                    reattach = True
                    self.device.detach_kernel_driver(0)

                cfg = usb.util.find_descriptor(self.device, bConfigurationValue=1)
                cfg.set()
                time.sleep(0.5)
                self.set_date()
                return True
        except ValueError:
            print('check_device Timeout error')
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
            ret = self.device.read(0x81, 3, 1000)
            self.start_condition = ret[2]
        except usb.core.USBTimeoutError:
            print('Write Timeout error')
        except usb.core.USBError:
            self.device = None

    def set_start_condition(self, cond: int = 0x21):
        if self.device is None:
            self.check_device()

        try:
            #print('set start cond')
            self.device.write(0x1, [0x21, cond], 1000)
            ret = self.device.read(0x81, 3, 1000)
            #print(f'start cond {ret}')
            self.start_condition = ret[2]
        except usb.core.USBTimeoutError:
            print('set_start_condition Timeout error')
        except usb.core.USBError:
            self.device = None

    def get_available_sensors(self, sensors: list[Sensor]):
        if self.device is None:
            self.check_device()
        if self.device is None:
            for s in sensors:
                s.connected = False

        try:
            #self.device.write(0x1, [ReportId.REPORT_OUT, UsbCmd.SENSOR_NUM], 1000)
            self.device.write(0x1, [0x21, 0x11], 1000)
            ret = self.device.read(0x81, 10, 1000)
            if ret[1] == 17:
                for i, s in enumerate(sensors):
                    if ret[i+2] != 0:
                        s.connected = True
                        s.who_am_i = ret[i+2]
                        s.name = sensor_name[s.who_am_i]
                    else:
                        s.connected = False
                        s.who_am_i = 0
                        s.name = None
                    #print(i, s.connected)
        except usb.core.USBTimeoutError:
            print("get_available_sensors Timeout error")
        except usb.core.USBError:
            self.device = None
        except AttributeError:
            pass

    def get_data_from_sensor(self, sensor: Sensor) -> float:
        if self.device is None:
            self.check_device()
        if self.device is not None and sensor.connected:
            #print('sens get data')
            try:
                if self.start_condition == 0:
                    self.set_start_condition(0x20)
                # print(index_to_cmd[sensor.id])
                self.device.write(0x1, [0x21, index_to_cmd[sensor.id]], 1000)
                ret = self.device.read(0x81, 8, 1000)
                data = (ctypes.c_char*4)()
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
            except usb.core.USBError:
                print("USB ERR get data")
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
            ret = self.device.read(0x81, 3, 1000)
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
        #print(r1, r2, r3)
        return r1, r2, r3
