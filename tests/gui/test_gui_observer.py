import unittest
from unittest.mock import patch

from lumi.core.statushandler import StatusHandler
from lumi.core.event import Event


class TestGUIObserver(StatusHandler):
    """StatusHandler can have two functions, 
        - first, its methods can be fired (attaching a method to an event name)
        through the Event fire() method (see the rest of this test),
        - second, you can override the on_pushed_status method that's fired everytime
        the push() method of this class is used. (see test_gui_status_handler test)"""

    """this class creates a custom status handler in order to add a test event callback"""

    def test_callback(self, data):
        try:
            self.called += 1
        except AttributeError as e:
            self.called = 1


class TestGuiObserver(unittest.TestCase):
    def _initialize_status_handler(self):
        self.status_handler = TestGUIObserver()

    def _attach_event_name_to_callback(self, event_name, callback):
        self.status_handler.observe(event_name, callback)

    def test_start_gui_status_handler(self):
        try:
            self._initialize_status_handler()
            self._attach_event_name_to_callback(
                event_name="example_event", callback=self.status_handler.test_callback
            )
        except Exception as e:
            self.fail(msg="%s exception raised!" % e)

        try:
            self.event = Event(name="example_event").fire()
            self.event = Event(name="example_event", data=1).fire()
        except Exception as e:
            self.fail(msg="%s exception raised" % e)
        self.assertEqual(self.status_handler.called, 1)


if __name__ == "__main__":
    unittest.main(exit=False)
