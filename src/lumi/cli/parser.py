from argparse import ArgumentParser

def get_parser():
    parser = ArgumentParser(description="Lumi CLI")
    subparsers = parser.add_subparsers(dest="action")

    add = subparsers.add_parser("add", description="Add a distro/stage to a device", help="add <device> <distro>")

    delete = subparsers.add_parser("delete", description="Delete a distro/stage from a device", help="delete <device> <distro>")

    install = subparsers.add_parser("install", description="Install Lumi on a device")

    list_p = subparsers.add_parser("list", )

    list_all = subparsers.add_parser("list-all")

    show = subparsers.add_parser("show-device")

    show = subparsers.add_parser("show-system")

    sync = subparsers.add_parser("sync")

    return parser
