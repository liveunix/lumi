import sys
from lumi.cli import dispatcher
from lumi.cli.parser import get_parser


def main():
    parser = get_parser()

    """Print usage when no action is issued"""
    if len(sys.argv[1:])==0:
        parser.print_help()
        parser.exit()

    action = parser.parse_args(sys.argv[1:])

    dispatcher.dispatch(action)


if __name__ == "__main__":
    main()
