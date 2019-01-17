from lumi.cli import parser
from lumi.cli import dispatcher


def main():
    dispatcher.dispatch(parser.parse_args())


if __name__ == "__main__":
    main()
