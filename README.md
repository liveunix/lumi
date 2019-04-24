# LUMI ( LiveUnix Multiboot ISO )

LUMI manages live images and stages of various systems (_UNIX_ based) on a removable device,
letting the user choose one live image on boot (using GRUB).

## CLI

Here it's a list of all the available commands:

Command                                          | Description                                                   | Example
------------------------------------------------ | -----------------------------------------------------------   | -----------------------------------
`lumi` or `lumi -h`                              | Get Lumi usage
`lumi add <name:version> <device>`               | Add the live image (or stage) on the device                   | `lumi add exherbo:20180618 /dev/sdb`
`lumi show-device <device>`                      | Show live images and stages present on the device             | `lumi show-device /dev/sdb`
`lumi show-system <name>`                        | Show information about a given system                         | `lumi show-system parabola`
`lumi delete <distro:version> <device>`          | Remove the live image (or stage) from the device              | `lumi delete ubuntu:18.04 /dev/sdb`
`lumi list-all`                                  | List all the available systems                                | `lumi list-all --stage3`
`lumi list <name>`                               | List all the live images and stages available for that system | `lumi list antergos`
`lumi sync`                                      | Sync the LUMI database                                        | `lumi sync`
`lumi [command] -h` or `lumi [command] --help`   | Get information about the commands or a specific one          | `lumi list-all --help`
=======
## Contributing

### Installation

We recommend to use `virtualenv` as environment for Python development.

```shell
virtualenv venv
```

Clone this repository:

```shell
git clone git@github.com:liveunix/lumi
```

Then switch to _virtualenv_ and install the dependencies:

```shell
source venv/bin/activate
venv/bin/pip install -r requirements.txt
```

## License

**LUMI** is licensed under [GNU/GPL v3](LICENSE).
