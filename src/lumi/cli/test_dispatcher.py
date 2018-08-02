import unittest
from .dispatcher import dispatch
from .parser import parse_args
from .actions.version import VERSION

class TestDispatcher(unittest.TestCase):
    """Test the LUMI action dispatcher"""
    def test_dispatcher_call_function(self):
        action = parse_args(['install', '/dev/sdb'])
        response = dispatch(action, callback=lambda _: True)
        self.assertTrue(response)

    def test_dispatcher_call_action_file(self):
        action = parse_args(['version'])
        response = dispatch(action)
        self.assertEqual(response, VERSION)
