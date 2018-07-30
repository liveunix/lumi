from sys import platform
import unix

def grub_install(device):
    if platform == "linux2" or platform == "darwin":
        unix.check_device(device)
        unix.check_grub_executable
    elif platform == "win32":
        # Windows...
        pass

if __name__ == "__main__":
