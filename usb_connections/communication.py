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
               0xBE: "Датчик пульса", 0xBB: "Датчик  освещенности", 0xBF: "Датчик ультрафиолета",
               0xB1: "Датчик давления", 0xB2: "Датчик влажности", 0xB3: "Датчик температуры"}

sensor_unit = {0xBD: "дБ", 0xBC: "°C", 0xBA: "A",
               0xBE: "", 0xBB: "люкс", 0xBF: "Вт/(м²)",
               0xB1: "Па", 0xB2: "%", 0xB3: "°C"}
sensor_val = {0xBD: "p", 0xBC: "T", 0xBA: "I",
               0xBE: "", 0xBB: "E", 0xBF: "E",
               0xB1: "p", 0xB2: "H", 0xB3: "T"}
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


class SdFile:
    def __init__(self, date: datetime, fb: int, lb: int, size: float, fb_b: list[int], lb_b: list[int]):
        self.date: datetime = date
        self.fb: int = fb
        self.lb: int = lb
        self.size: float = size
        self.fb_b: list[int] = fb_b
        self.lb_b: list[int] = lb_b


class SensorSd:
    def __init__(self, index: int):
        self.id: int = index
        self.available: bool = False
        self.who_am_i: int | None = None
        self.name: str | None = None
        self.x: list = []
        self.y: list = []
        self.dataset: dict = {"Время": []}

    def parse_dataset(self, data):
        id_to_data_idx = 5 * self.id + 9
        # print(id_to_data_idx)
        wai = data[id_to_data_idx]
        date = datetime(year=localtime().tm_year,
                        month=data[2],
                        day=data[3],
                        hour=data[4],
                        minute=data[5],
                        second=data[6],
                        microsecond=(999 - data[7]) * 1000)
        time_sd = date.strftime("%Y-%m-%d %H:%M:%S:%f")

    def parse_first_sd_data(self, data):
        id_to_data_idx = 5*self.id + 9
        # print(id_to_data_idx)
        wai = data[id_to_data_idx]

        if wai != 0:

            #print(data)
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
            if wai == 0xBE and data_v == -999:
                data_v = 0
            elif wai == 0xBE:
                data_v = int(data_v)
            elif wai == 0xBF and abs(data_v) < 0.55:
                data_v = 0.0
            # print(self.x, self.y)
            self.y.append(data_v)
            self.x.append(0)
            # self.dataset["Время"].append(time_sd)
            self.dataset['Время эксперимента'] = []
            self.dataset[f'Значение, {sensor_unit[self.who_am_i]}'] = []

    def parse_sd_data(self, data):
        id_to_data_idx = 5 * self.id + 9
        # print(f'parse sd data {id_to_data_idx} {data}')
        # print(id_to_data_idx)
        wai = data[id_to_data_idx]
        if wai != 0:
            if wai != self.who_am_i:
                return
            self.available = True
            self.name = sensor_name[self.who_am_i]
            date = datetime(year=localtime().tm_year,
                            month=data[2],
                            day=data[3],
                            hour=data[4],
                            minute=data[5],
                            second=data[6],
                            microsecond=(999 - data[7]) * 1000)
            time_sd = date.strftime("%Y-%m-%d %H:%M:%S:%f")
            time_sd = time_sd[:-3]

            datac = (ctypes.c_char * 4)()
            datac[0] = data[id_to_data_idx + 1]
            datac[1] = data[id_to_data_idx + 2]
            datac[2] = data[id_to_data_idx + 3]
            datac[3] = data[id_to_data_idx + 4]
            data_f = struct.unpack('f', bytes(datac))
            data_v = round(data_f[0], 2)
            # print(self.who_am_i)
            if wai == 0xBE and data_v == -999:
                data_v = 0
            elif wai == 0xBE:
                data_v = int(data_v)
            elif wai == 0xBF and abs(data_v) < 0.55:
                data_v = 0.0
            if not self.x:
                self.x.append(0)
            else:
                self.x.append(self.x[-1] + 1)
            if self.who_am_i == 0xBE:
                if data_v < -1:
                    data_v = 0
            self.y.append(data_v)
            self.dataset["Время"].append(time_sd)
            time0 = datetime.strptime(self.dataset['Время'][0]+'000', "%Y-%m-%d %H:%M:%S:%f")
            time1 = datetime.strptime(time_sd+'000', "%Y-%m-%d %H:%M:%S:%f")
            timestamp = round((time1 - time0).total_seconds(), 2)
            self.dataset["Время эксперимента"].append(timestamp)
            self.dataset[f'Значение, {sensor_unit[self.who_am_i]}'].append(data_v)



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
        self.y: list[int | float] = [0 for _ in range(100)]
        self.x_time = list()
        self.x_timestamp = list()
        self.timestamp: float = 0.0


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
        self.sd_files: list = []
        self.stop = 0
        self.sd_file: list = list()
        self.load_app_started = False
        self.load_app = []
        # self.time = time.time()

    def parse_sd_file(self, data: list):
        date = datetime(year=localtime().tm_year,
                        month=data[2],
                        day=data[3],
                        hour=data[4],
                        minute=data[5],
                        second=data[6],
                        microsecond=(999 - data[7])*1000)
        one_mesurement = []
        time_sd = date.strftime("%Y-%m-%d %H:%M:%S:%f")
        one_mesurement.append(time_sd)
        for i in range(11):
            one_mesurement.append(data[9+i*5])
            datac = (ctypes.c_char * 4)()
            datac[0] = data[10 + i*5]
            datac[1] = data[11 + i*5]
            datac[2] = data[12 + i*5]
            datac[3] = data[13 + i*5]
            data_f = struct.unpack('f', bytes(datac))
            data_v = round(data_f[0], 2)
            if data[9+i*5] == 0xBE and data_v == -999:
                data_v = 0
            elif data[9+i*5] == 0xBE:
                data_v = int(data_v)
            elif data[9+i*5] == 0xBF and abs(data_v) < 0.55:
                data_v = 0.0
            one_mesurement.append(data_v)
        self.sd_file.append(one_mesurement)
        # print(one_mesurement)

    def check_device(self) -> bool:
        try:
            dev = None
            # print(platform)
            libusb1_backend = usb.backend.libusb1.get_backend(find_library=libusb_package.find_library)
            # print(libusb1_backend)
            # dev = usb.core.find(idVendor=self.vid, idProduct=self.pid)
            # print(dev)
            # dev.set_configuration()
            if platform == "linux" or platform == "linux2":
                # print(f"LINUX {platform}")
                dev = usb.core.find(idVendor=self.vid, idProduct=self.pid)

                # dev.set_configuration()
            elif platform == "win32":
                # print(f"WINDOWS {platform}")
                dev = libusb_package.find(idVendor=self.vid, idProduct=self.pid, backend=libusb1_backend)

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
            if self.stop or self.load_app_started:
                return
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

    def get_data_from_sensor(self, sensor: Sensor) -> float | None:

        if self.device is None:
            self.check_device()
        if self.device is not None and sensor.connected:
            # print('sens get data')
            try:
                if self.stop == 1 or self.load_app_started:
                    return
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
                    data_v = 0
                elif ret[2] == 0xBE:
                    data_v = int(data_v)
                elif ret[2] == 0xBF and abs(data_v) < 0.55:
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
        if not self.device:
            return
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
        if not self.device:
            return
        try:
            self.device.write(0x1, [0x21, 0x27], 1000)
            ret = self.device.read(0x81, 64, 1000)
            #print(ret)
            self.sd_files.clear()

            data = (ctypes.c_char * 4)()
            for i in range(4):
                if ret[8+i*14] == 0 or ret[9+i*14] == 0:
                    continue
                date = datetime(year=2000 + ret[7 + i*14],
                                month=ret[8 + i*14],
                                day=ret[9 + i*14],
                                hour=ret[10 + i*14],
                                minute=ret[11 + i*14],
                                second=ret[12 + i*14])
                data[0] = ret[13 + i*14]
                data[1] = ret[14 + i*14]
                data[2] = ret[15 + i*14]
                data[3] = ret[16 + i*14]
                fb = struct.unpack('I', bytes(data))[0]
                data[0] = ret[17 + i*14]
                data[1] = ret[18 + i*14]
                data[2] = ret[19 + i*14]
                data[3] = ret[20 + i*14]
                lb = struct.unpack('I', bytes(data))[0]
                size = round((lb - fb) * 496 / 1024, 2)
                # print(date)
                self.sd_files.append(SdFile(date, fb, lb, size,
                                            [ret[13 + i*14], ret[14 + i*14], ret[15 + i*14], ret[16 + i*14]],
                                            [ret[17 + i*14], ret[18 + i*14], ret[19 + i*14], ret[20 + i*14]]))
            self.sd_files.sort(key=lambda x: x.date, reverse=True)
            self.sd_checked = True
            if len(self.sd_files) == 0:
                self.sd_empty = 1
            else:
                self.sd_empty = False

        except usb.core.USBTimeoutError as e:
            print(f"get_sd_info Timeout error {e}")
        except usb.core.USBError as e:
            print(f"USB ERR get_sd_info {e}")
        except AttributeError:
            print("ATTRIBUTE ERR get_sd_info")

    def get_sd_data(self, sensors: list[SensorSd], index: int):
        if not self.device:
            return
        for i in sensors:
            i.available = False
        try:
            self.device.write(0x1, [0x23, 0x30,
                                    self.sd_files[index].fb_b[0], self.sd_files[index].fb_b[1],
                                    self.sd_files[index].fb_b[2], self.sd_files[index].fb_b[3],
                                    self.sd_files[index].lb_b[0], self.sd_files[index].lb_b[1],
                                    self.sd_files[index].lb_b[2], self.sd_files[index].lb_b[3]], 1000)
            ret = self.device.read(0x81, 64, 1000)

            self.device.write(0x1, [0x21, 0x28], 1000)
            ret = self.device.read(0x81, 64, 1000)
            self.stop = 1

            for i in sensors:
                i.parse_first_sd_data(ret)
            while ret[1] != 1:

                self.device.write(0x1, [0x21, 0x28], 2000)
                ret = self.device.read(0x81, 64, 1000)
                # print(ret)
                self.parse_sd_file(ret)
                if ret[0] == 16:
                    for i in sensors:
                        i.parse_sd_data(ret)
            self.stop = 0
            self.data_downloaded = True
        except usb.core.USBTimeoutError as e:
            print(f"get_sd_data Timeout error {e}")
        except usb.core.USBError as e:
            print(f"USB ERR get_sd_data {e}")
        except AttributeError:
            print("ATTRIBUTE ERR get_sd_data")

    def send_exit(self):
        if not self.device:
            return
        try:
            self.device.write(0x1, [0x21, 0x29], 1000)
            ret = self.device.read(0x81, 64, 1000)
            # print(ret)
        except usb.core.USBTimeoutError as e:
            print(f"send_exit Timeout error {e}")
        except usb.core.USBError as e:
            print(f"USB ERR send_exit {e}")
        except AttributeError:
            print("ATTRIBUTE ERR send_exit")

    def send_who_am_i(self, who_am_i: int):
        if not self.device:
            return
        try:
            self.device.write(0x1, [0x24, 0x31, who_am_i], 1000)
            ret = self.device.read(0x81, 64, 1000)
        except usb.core.USBTimeoutError as e:
            print(f"send_who_am_i Timeout error {e}")
        except usb.core.USBError as e:
            print(f"USB ERR send_who_am_i {e}")
        except AttributeError:
            print("ATTRIBUTE ERR send_who_am_i")

    def clear_sd(self):
        if not self.device:
            return
        try:
            self.device.write(0x1, [0x21, 0x35], 1000)
            ret = self.device.read(0x81, 64, 1000)
        except usb.core.USBTimeoutError as e:
            print(f"clear sd Timeout error {e}")
        except usb.core.USBError as e:
            print(f"USB ERR clear sd {e}")
        except AttributeError:
            print("ATTRIBUTE ERR clear sd")

    def load_new_app(self):
        if not self.device:
            return
        self.load_app_started = True
        try:

            for i in range(3584):
                if i == 3583:
                    data_transmit = [0x25, 0x32, 1] + self.load_app[i*32:i*32+32]
                else:
                    data_transmit = [0x25, 0x32, 0] + self.load_app[i * 32:i * 32 + 32]
                self.device.write(0x1, data_transmit, 1000)
                ret = self.device.read(0x81, 64, 1000)
                print(i, ret)
        except usb.core.USBTimeoutError as e:
            print(f"clear sd Timeout error {e}")
        except usb.core.USBError as e:
            print(f"USB ERR clear sd {e}")
        except AttributeError:
            print("ATTRIBUTE ERR clear sd")
        finally:
            self.load_app_started = False
