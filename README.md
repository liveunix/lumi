# LUMI

## CLI

LUMI comes with a command-line interface you can use to easily manage distros.

Here it's a list of all the available commands:

| Command                                    | Description                                     | Example                           |
| ------------------------------------------ | ----------------------------------------------- | --------------------------------- |
| lumi install \<device\>                    | Install LUMI on a device                        | lumi install /dev/sdb             |
| lumi inspect \<device\>                    | Inspect device for the installed distros        | lumi inspect /dev/sdb             |
| lumi sync                                  | Sync the LUMI database                          | lumi sync                         |
| lumi list-all                              | List all the available distros                  | lumi list-all                     |
| lumi list-all \<distro\>                   | List all the versions available for that distro | lumit list-all antergos           |
| lumi add \<distro:version\> \<device\>     | Install the distro installer on the device      | lumi add ubuntu:18.04 /dev/sdb    |
| lumi delete \<distro:version\> \<device\>  | Remove the distro installer from the device     | lumi delete ubuntu:18.04 /dev/sdb |
| lumi -h or lumi help                       | Get information about LUMI                      ||

## License

**LUMI** is licensed under [GNU/GPL v3](LICENSE).
