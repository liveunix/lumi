# lumi ( LiveUnix Multiboot Iso )

lumi manages live images and stages of various systems (_UNIX_ based) on a removable device,
letting the user choose one live image on boot (using GRUB).

## CLI

Here it's a list of all the available commands:

Command                                 | Description                                                      | Example
--------------------------------------- | -----------------------------------------------------------      | -----------------------------------
`lumi`                                  | Get lumi usage
`lumi setup <device>`                   | Setup lumi on a device                                           | `lumi setup /dev/sdb1`
`lumi add <name:version>...`            | Add the live image(s) or stage(s) on a device                    | `lumi add arch:2019.04.01`
`lumi show <device>`                    | Show live images and stages present on the device                | `lumi show /dev/sdb`
`lumi show <name:version>`              | Show information about a given system and its live images/stages | `lumi show parabola`
`lumi delete <name:version>..`          | Remove the live image (or stage) from the device                 | `lumi delete ubuntu:18.04`
`lumi list`                             | List all the live images and stages available for that system    | `lumi list exherbo`
`lumi update`                           | Update all the systems
`lumi sync`                             | Update the systems database
`lumi [command] -h`                     | Get information about the commands or a specific one             | `lumi list -h`

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
