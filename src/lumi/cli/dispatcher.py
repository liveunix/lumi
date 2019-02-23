import sys
from lumi.cli import actions
from lumi.cli.parser import get_parser


def dispatch():
    parser = get_parser()

    """Print usage when no action is issued"""
    if len(sys.argv[1:])==0:
        parser.print_help()
        parser.exit()

    action = parser.parse_args(sys.argv[1:])

    if action is None:
        return

    """Invoke the right callback for the given action"""
    try:
        module = getattr(actions, action.command)
    except:
        return

    callback = getattr(module, "dispatch", lambda action: False)
    callback(action)
