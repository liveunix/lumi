OPTIONS = [
    {
        "shortcut": "-3",
        "extended": "--stage3",
        "action": "store_true",
        "dest": "stage_three",
        "description": "Manage stage3 instead of distros",
    },
    {
        "shortcut": "-a",
        "extended": "--arch",
        "action": "store",
        "dest": "architecture",
        "description": "Specify architecture target for the distro or stage3",
    },
]


def register_options(argument_parser):
    """Register the available options for the given parser"""
    for option in OPTIONS:
        argument_parser.add_argument(
            option["shortcut"],
            option["extended"],
            action=option["action"],
            dest=option.get("dest") or None,
            help=option["description"],
        )
    return argument_parser
