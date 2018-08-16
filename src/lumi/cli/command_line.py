from . import parser
from . import dispatcher

def main():
    dispatcher.dispatch(parser.parse_args())

