import json
import sh
import libmount as mnt
from xdg.BaseDirectory import xdg_data_home

# Return True if device is mounted
def is_device_mounted(device_uuid):
    if get_mountpoint(device_uuid) == None:
        return False
    return True

# Mount a device
def mount(device_uuid):
    if is_device_mounted(device_uuid):
        raise Exception("Device is already mounted")

# Get info about a single device, device arg should the name (eg. /dev/sdc1)
def get_device_data(data_cols, device):
    output = json.loads(sh.lsblk(device, paths=True, nodeps=True, inverse=True, json=True, output=data_cols ).stdout)
    return output['blockdevices'][0]

# Get filesystems and partitions
def get_devices_data(data_cols):
    output = json.loads(sh.lsblk(paths=True, nodeps=True, inverse=True, json=True, output=data_cols).stdout)
    return output['blockdevices']

# Get uuid from a device name
def get_uuid(device):
    device_fs = sh.blkid('--uuid', device_uuid).stdout.strip()

def get_mountpoint(device_uuid):
    device_fs = sh.blkid('--uuid', device_uuid).stdout.strip()
    info = get_device_data('MOUNTPOINT,UUID', device_fs)

    # If the uuid returned by lsblk is different then the one we passed to blkid
    # it means that another device has replaced the one we were working on
    if info['uuid'] != device_uuid:
        raise Exception("Device has been changed")

    return info['mountpoint']

# Get the next available mount point
def get_new_mount_target():
    # Start from -1 because there is an increment at the start
    i = -1
    # Path where the device should be mounted
    target_path = xdg_data_home + '/lumi/dev'
    is_available = False

    # While we have not found a valid path available
    df = sh.df(portability=True).stdout.decode('utf-8')
    while not is_available:
        i += 1
        is_available = True
        for s in df.split('\n')[1:]:
            # It is not long enough to contain the column we need
            if len(s) < 6:
                continue
            if target_path + str(i) == s.split()[5].strip():
                is_available = False

    return target_path + str(i)


# Get all devices suitable for installation
def get_devices():
    devices = get_devices_data('NAME,LABEL,UUID,RM,MOUNTPOINT')
    suitable_devices = []

    for d in devices:
        if d['rm'] == '1':
            suitable_devices.append(d.copy())

    return suitable_devices

# Get all devices loaded in lumi
def get_enabled_devices():
    pass

