import unittest
from lumi.gui.guimanager.statushandler import GUIStatusHandler


class CustomStatusHandler(GUIStatusHandler):
    """StatusHandler can have two functions, 
        - first, its methods can be fired, attaching a method to an event name,
        through the Event fire() method (see the test_gui_observer test),
        - second, you can override the on_pushed_status method that's fired everytime
        the push() method of this class is used. (see the rest of this test)"""

    def on_pushed_status(self, data):
        # this function will be called whenever an item is pushed to status handler
        # this is an example override for the tests
        self.pushed_status_called = True


class TestGUIStatusHandler(unittest.TestCase):
    first_element = 1
    second_element = "string"

    def test_push_status(self):
        status_handler_first = CustomStatusHandler()
        status_handler_second = CustomStatusHandler()

        status_handler_first.push(self.first_element)

        status_handler_first.push(self.second_element)

        self.assertEqual(len(status_handler_second._statuses), 2)

        self.assertEqual(status_handler_second._statuses[0], self.first_element)
        self.assertEqual(status_handler_second._statuses[1], self.second_element)

    def test_pop_status(self):
        status_handler_first = CustomStatusHandler()

        status_handler_second = CustomStatusHandler()

        status_handler_second.push(self.first_element)

        status_handler_second.push(self.second_element)

        popped_first_element = status_handler_first.pop()
        popped_second_element = status_handler_first.pop()

        self.assertEqual(len(status_handler_first._statuses), 0)

        self.assertEqual(self.first_element, popped_second_element)
        self.assertEqual(self.second_element, popped_first_element)

    def test_on_pushed_item_callback(self):
        status_handler = CustomStatusHandler()

        status_handler.push(self.first_element)
        status_handler.pop()  # empty statuses

        self.assertTrue(status_handler.pushed_status_called)


if __name__ == "__main__":
    unittest.main()
