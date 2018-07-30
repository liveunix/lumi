from shutil import which
import subprocess

# Return True if device is mounted
def is_device_mounted(device):
    df = subprocess.run('df', stdout=subprocess.PIPE).stdout.decode('utf-8')
    for lines in df[1:].splitlines():
        if lines.split()[0] == device:
            return True
    return False

# Mount a device
def mount(device):
    # Use fdisk
    pass

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

