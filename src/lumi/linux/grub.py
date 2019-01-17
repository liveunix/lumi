from pathlib import Path
import sh


def install(partition_fs):
    partition = get_partition(partition_fs)

    grub_i386_dir = Path("/usr/lib/grub/i386-pc")
    if grub_i386_dir.exists():
        grub_i386_supported = True
        sh.contrib.sudo(
            "grub-install",
            partition_fs[:-1],
            boot_directory=partition["mountpoint"] + "/boot",
            target="i386-pc",
            removable=True,
        )
    else:
        grub_i386_supported = False

    grub_efi_dir = Path("/usr/lib/grub/x86_64-efi")
    if grub_efi_dir.exists():
        grub_efi_supported = True
        sh.contrib.sudo(
            "grub-install",
            partition_fs[:-1],
            efi_directory=partition["mountpoint"],
            target="x86_64-efi",
            bootloader_id="lumi",
            removable=True,
        )
    else:
        grub_efi_supported = False

    return sh.grub_install(version=True)


def update(partition_fs):
    mountpoint = get_partition(partition_fs)["mountpoint"]

    sh.contrib.sudo.rm(mountpoint + "/EFI", recursive=True, force=True)
    sh.contrib.sudo.rm(mountpoint + "/boot/grub", recursive=True, force=True)

    return install_grub(partition_fs)


def install_theme(partition_fs):
    pass
