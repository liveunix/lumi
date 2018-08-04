# LUMI ( LiveUnix Multiboot ISO )

## CLI

LUMI comes with a command-line interface you can use to easily manage distros.

Here it's a list of all the available commands:

| Command                                                    | Description                                                 | Example                                      |
| ---------------------------------------------------------- | ----------------------------------------------------------- | -------------------------------------------- |
| `lumi install <device>`                                    | Install LUMI on a device                                    | `lumi install /dev/sdb`                      |
| `lumi inspect <device>`                                    | Inspect device for the installed distros                    | `lumi inspect /dev/sdb`                      |
| `lumi sync`                                                | Sync the LUMI database                                      | `lumi sync`                                  |
| `lumi list-all`                                            | List all the available distros                              | `lumi list-all --stage3`                     |
| `lumi list <name>`                                         | List all the versions available for that distro or stage3   | `lumi list antergos`                         |
| `lumi add <name:version> <device>`                         | Add the distro (or stage3) installer on the device          | `lumi add exherbo:20180618 /dev/sdb -a i686` |
| `lumi delete <distro:version> <device>`                    | Remove the distro (or stage3) installer from the device     | `lumi delete ubuntu:18.04 /dev/sdb`          |
| `lumi [command] -h` or `lumi [command] --help`             | Get information about the commands or a specific one        | `lumi list-all --help`                       |
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
