# LUMI

## CLI

LUMI comes with a command-line interface you can use to easily manage distros.

Here it's a list of all the available commands:

| Command                                                   | Description                                                 | Example                                    |
| --------------------------------------------------------- | ----------------------------------------------------------- | ------------------------------------------ |
| lumi install \<device\>                                   | Install LUMI on a device                                    | lumi install /dev/sdb                      |
| lumi inspect \<device\>                                   | Inspect device for the installed distros                    | lumi inspect /dev/sdb                      |
| lumi sync                                                 | Sync the LUMI database                                      | lumi sync                                  |
| lumi list-all [-3 or -stage3]                             | List all the available distros                              | lumi list-all                              |
| lumi list \<name\> [-3 or -stage3]                        | List all the versions available for that distro or stage3   | lumit list-all antergos                    |
| lumi add \<name:version\> \<device\> \[-3 or -stage3\] [-arch=arch]     | Add the distro (or stage3) installer on the device          | lumi add exherbo:20180618 /dev/sdb -stage3 -arch=x86_64 |
| lumi delete \<distro:version\> \<device\> [-3 or -stage3] | Remove the distro (or stage3) installer from the device     | lumi delete ubuntu:18.04 /dev/sdb          |
| lumi [command] -h or lumi [command] --help                | Get information about the commands or a specific one        | lumi list-all --help                       |

**You can manage stage3 instead of distros by adding the flag `-3` or `-stage3`.**

## License

**LUMI** is licensed under [GNU/GPL v3](LICENSE).
