SUBCOMMANDS = [
    {"command": "help", "require_options": False, "description": "", "arguments": []},
    {
        "command": "install",
        "description": "Install LUMI on a device",
        "arguments": [
            {
                "name": "device",
                "type": str,
                "help": "The device where install LUMI (e.g. /dev/sdb)",
            }
        ],
    },
    {
        "command": "search",
        "description": "List all the systems that match the query",
        "arguments": [
            {
                "name": "query",
                "type": str,
                "help": "Query to match against all avaiable systems",
            }
        ],
    },
    {
        "command": "sync",
        "require_options": False,
        "description": "Sync the LUMI database",
        "arguments": [],
    },
    {
        "command": "list-all",
        "description": "List all the available distros and stage3",
        "arguments": [],
    },
    {
        "command": "list",
        "description": "List all the versions for a given distro or stage3",
        "arguments": [
            {
                "name": "device",
                "type": str,
                "help": "The device to get information from",
            }
        ],
    },
    {
        "command": "add",
        "description": "Add the distro (or stage3) installer on the device",
        "arguments": [
            {
                "name": "target",
                "type": str,
                "help": "The distro or stage3 name and version (e.g. ubuntu:18.04.1)",
            },
            {
                "name": "device",
                "type": str,
                "help": "The device to inspect (e.g. /dev/sdb)",
            },
        ],
    },
    {
        "command": "delete",
        "description": "Remove the distro (or stage3) installer from the device",
        "arguments": [
            {
                "name": "target",
                "type": str,
                "help": "The distro or stage3 name and version (e.g. ubuntu:18.04.1)",
            },
            {
                "name": "device",
                "type": str,
                "help": "The device to inspect (e.g. /dev/sdb)",
            },
        ],
    },
    {
        "command": "version",
        "require_options": False,
        "description": "",
        "arguments": [],
    },
]
