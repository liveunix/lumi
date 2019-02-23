from argparse import ArgumentParser
from sys import argv
from lumi.cli.subcommands import SUBCOMMANDS

def get_parser():
    parser = ArgumentParser(description="Lumi CLI")
    subparsers = parser.add_subparsers(dest="action")

    return parser
