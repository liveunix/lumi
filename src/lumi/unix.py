import subprocess
from xdg.BaseDirectory import xdg_data_home
from shutil import which

# Return True if device is mounted
# device is the uuid
def is_device_mounted(device):
    device_fs = subprocess.run(['blkid', '--uuid', device], stdout=subprocess.PIPE).stdout.decode('utf-8')
    df = subprocess.run(['df', '--output=source'], stdout=subprocess.PIPE).stdout.decode('utf-8')
    for lines in df.splitlines()[1:]:
        if lines.strip() == device_fs.strip():
            return True
    return False

# Mount a device
# device is a uuid
def mount(device):
    if is_device_mounted(device):
        raise Exception("Device is already mounted")

# Get the next available mount point
def get_new_mount_target():
    # Start from -1 because there is an increment at the start
    i = -1
    # Path where the device should be mounted
    target_path = xdg_data_home + '/lumi/dev'
    is_available = False
    # While we have not found a valid path available
    while not is_available:
        i += 1
        is_available = True
        df = subprocess.run(['df', '--output=target'], stdout=subprocess.PIPE).stdout.decode('utf-8')
        for s in df.splitlines()[1:]:
            if target_path + str(i) == s.strip():
                is_available = False

    return target_path + str(i)


# Get all devices suitable for installation
def get_devices():
    pass

# Get all devices loaded in lumi
def get_mounted_devices():
    pass

def check_grub_executable():
    grub_install_exe = which("grub-install2")
    if grub_install_exe == None:
        raise Exception("No grub-install executable in PATH")

