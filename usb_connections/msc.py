import os

import psutil
import re
import subprocess
from os import listdir
from os.path import isfile, join


def check_device() -> bool:
    device_re = re.compile(b"Bus\s+(?P<bus>\d+)\s+Device\s+(?P<device>\d+).+ID\s(?P<id>\w+:\w+)\s(?P<tag>.+)$", re.I)
    df = subprocess.check_output("lsusb")
    devices = []
    for i in df.split(b'\n'):
        if i:
            info = device_re.match(i)
            if info:
                dinfo = info.groupdict()
                dinfo['device'] = '/dev/bus/usb/%s/%s' % (dinfo.pop('bus'), dinfo.pop('device'))
                devices.append(dinfo)
    for i in devices:
        if i['tag'] == b'STMicroelectronics STM32 COMPOSITE DEVICE':
            return True
    return False


def get_device_path_linux() -> tuple[str, str] | None:
    if not check_device():
        return None
    d = psutil.disk_partitions(all=False)
    for i in d:
        if "uid=1000,gid=1000,fmask=0022,dmask=0022,codepage=437," in i.opts:
            # print(i)
            path = i.mountpoint
            onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
            for file in onlyfiles:
                # print(file[0:4], file[-4:])
                if "appv" in file[0:4] and ".bin" in file[-4:]:
                    return path, file
    return None


def write_bin_file_to_device(path_dev: str, file_name: str, data: bytes) -> bool:
    try:
        # with open(path_file, 'rb') as f:
        #    data = f.read()
        with open(path_dev + file_name, 'wb') as f:
            f.write(data)
    except Exception as e:
        print(f'Exception in writing .bin file to devive: {e}')
        return False
    return True


def remove_file(path, filename) -> bool:
    try:
        os.remove(path+'/'+filename)
        return True
    except Exception as e:
        print(f"Exception in remove old app file {e}")
        return False
