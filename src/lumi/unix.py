from shutil import which
import subprocess

# Return True if device is mounted
# device is the uuid
def is_device_mounted(device):
    device_fs = subprocess.run(['blkid', '--uuid', device], stdout=subprocess.PIPE).stdout.decode('utf-8')
    df = subprocess.run(['df', '--type=vfat', '--output=source'], stdout=subprocess.PIPE).stdout.decode('utf-8')
    for lines in df.splitlines()[1:]:
        if lines.strip() == device_fs.strip():
            return True
    return False

# Mount a device
def mount(device):
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

