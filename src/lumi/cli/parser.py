from argparse import ArgumentParser

def get_parser():
    parser = ArgumentParser(description="Lumi CLI")
    subparsers = parser.add_subparsers(dest="action")

    return parser
