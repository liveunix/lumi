import unittest
from src.lumi.cli.dispatcher import dispatch
from src.lumi.cli.parser import parse_args
from src.lumi.cli.actions.version import VERSION


class TestDispatcher(unittest.TestCase):
    """Test the LUMI action dispatcher"""

    def test_dispatcher_call_function(self):
        action = parse_args(["install", "/dev/sdb"], offset=0)
        response = dispatch(action, callback=lambda _: True)
        self.assertTrue(response)

    def test_dispatcher_call_action_file(self):
        action = parse_args(["version"], offset=0)
        response = dispatch(action)
        self.assertEqual(response, VERSION)
