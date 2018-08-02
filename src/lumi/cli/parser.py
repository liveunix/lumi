from argparse import ArgumentParser
from sys import argv
from .options import register_options
from .subcommands import SUBCOMMANDS

parser = ArgumentParser()
register_options(parser)
subparsers = parser.add_subparsers(dest='command')

for subcommand in SUBCOMMANDS:
    subparser = subparsers.add_parser(subcommand['command'], help=subcommand['description'])

    for argument in subcommand['arguments']:
        subparser.add_argument(argument['name'], type=argument['type'], help=argument['help'])

    if subcommand.get('require_options') is not False:
        register_options(subparser)


def parse_args(args=argv):
    """Parse the given commands using the declared parser"""
    return parser.parse_args(args)
