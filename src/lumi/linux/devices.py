import json
import sh
import libmount as mnt
from os import getuid, getgid
from pathlib import Path
from xdg.BaseDirectory import xdg_data_home

# Return True if device is mounted
def is_partition_mounted(device_fs):
    if get_mountpoint(device_fs) == None:
        return False
    return True

# Mount a partition in the selected mountpoint
def mount(partition_fs, mountpoint):
    if is_partition_mounted(device_fs):
        raise Exception("Device is already mounted")

    sh.sudo.mount(partition_fs, mountpoint, uid=getuid(), gid=getgid(), chmod='0777')

# Get info about a single device, device arg should the name (eg. /dev/sdc1)
def get_partition(partition_name):
    output = json.loads(sh.lsblk(partition_name, paths=True, nodeps=True, inverse=True, json=True, output='NAME,UUID,RM,FSTYPE,MOUNTPOINT').stdout)
    return output['blockdevices'][0]

def get_partition_filesystem(device_uuid):
    return sh.blkid('--uuid', device_uuid).stdout.strip()

def get_mountpoint(device_fs):
    info = get_partition(device_fs)
    return info['mountpoint']

# Has the device been replaced?
def has_partition_changed(device_fs):
    device_fs = get_partition(device_fs)
    for d in get_enabled_partitions():
        # If the uuid returned by lsblk is different then the one we passed to blkid
        # it means that another device has replaced the one we were working on
        if d['name'] == device_fs and info['uuid'] != device_uuid:
            raise Exception("Device has been changed")

# Get the next available mount point
# Check all devices mounted, not only the one handled by lumi
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
def get_all_devices():
    devices = json.loads(sh.lsblk(paths=True, nodeps=True, json=True, output='NAME,RM,MOUNTPOINT,UUID,FSTYPE,LABEL,CHILDREN').stdout)
    suitable_devices = []

    for d in devices['blockdevices']:
        if d['rm'] == '1' and len(d['children']) == 1:
            suitable_devices.append(d.copy())

    return suitable_devices

# Get all partitions loaded in lumi
def get_enabled_partitions():
    partition_file = xdg_data_home + "/lumi/status.json"

    with open(partition) as json_data:
        partitions = json.load(json_data)
        return partitions

def add_enabled_partition(partition_fs):
    data_file = xdg_data_home + "/lumi/status.json"

    with open(data_file, 'a') as json_data:
        partitions = json.load(json_data)

        partition_data = get_partition(partition_fs)

        # Check for a davice with the same uuid, to avoid re-adding a device
        for d in partitions:
            if d['uuid'] == partition_data['uuid']:
                raise Exception("Device already enabled")

        partition_status = Path(partition_data['mountpoint'] + '/lumi.json')
        if not partition_status.exists():
            partition_data['installed'] = False
        else:
            partition_data['installed'] = True

        json_data.write(json.dumps(device_data))

