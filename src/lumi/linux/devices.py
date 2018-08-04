import json
import sh
import libmount as mnt
from os import getuid, getgid
from pathlib import Path
from xdg.BaseDirectory import xdg_data_home

def is_partition_mounted(device_fs):
    """Return True if device is mounted"""
    if get_mountpoint(device_fs) == None:
        return False
    return True

def mount(partition_fs, mountpoint):
    """Mount a partition in the selected mountpoint"""
    if is_partition_mounted(device_fs):
        raise Exception("Device is already mounted")

    sh.sudo.mount(partition_fs, mountpoint, uid=getuid(), gid=getgid(), chmod='0777')

def get_partition(partition_name):
    """Get info about a single device (e.g. /dev/sdc1)"""
    output = json.loads(sh.lsblk(partition_name, paths=True, nodeps=True, inverse=True, json=True, output='NAME,UUID,RM,FSTYPE,MOUNTPOINT').stdout)
    return output['blockdevices'][0]

def get_partition_filesystem(device_uuid):
    return sh.blkid('--uuid', device_uuid).stdout.strip()

def get_mountpoint(device_fs):
    info = get_partition(device_fs)
    return info['mountpoint']

def has_partition_changed(device_fs):
    """Check if the device has been replaced"""
    device_fs = get_partition(device_fs)
    for d in get_enabled_partitions():
        # If the uuid returned by lsblk is different then the one we passed to blkid
        # it means that another device has replaced the one we were working on
        if d['name'] == device_fs and info['uuid'] != device_uuid:
            raise Exception("Device has been changed")

def get_new_mount_target():
    """Get the next available mount point.
       Check all the mounted devices, not only the one handled by LUMI.
    """
    i = -1
    target_path = xdg_data_home + '/lumi/dev'

    df = sh.df(portability=True).stdout.decode('utf-8')
    while valid_path_found is False:
        i += 1
        valid_path_found = True
        for s in df.split('\n')[1:]:
            # It is not long enough to contain the column we need
            if len(s) < 6:
                continue
            if target_path + str(i) == s.split()[5].strip():
                valid_path_found = False

    return target_path + str(i)

def get_all_devices():
    """Get all the devices available for the installation"""
    devices = json.loads(sh.lsblk(paths=True, nodeps=True, json=True, output='NAME,RM,MOUNTPOINT,UUID,FSTYPE,LABEL,CHILDREN').stdout)
    suitable_devices = []

    for d in devices['blockdevices']:
        if d['rm'] == '1' and len(d['children']) == 1:
            suitable_devices.append(d.copy())

    return suitable_devices

def get_enabled_partitions():
    """Get all the actively used partitions"""
    partition_file = xdg_data_home + "/lumi/status.json"

    with open(partition) as json_data:
        partitions = json.load(json_data)
        return partitions

def add_enabled_partition(partition_fs):
    """Update the file containing the enabled devices"""
    data_file = xdg_data_home + '/lumi/status.json'

    with open(data_file, 'a') as json_data:
        partitions = json.load(json_data)
        partition_data = get_partition(partition_fs)

        # Check if the given device is already enabled
        for d in partitions:
            if d['uuid'] == partition_data['uuid']:
                raise Exception("Device already enabled")

        partition_status = Path(partition_data['mountpoint'] + '/lumi.json')
        installed = True

        if partition_status.exists() is False:
            installed = False

        partition_data['installed'] = installed
        json_data.write(json.dumps(device_data))
