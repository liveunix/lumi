from application_window_class_test import TestApplicationWindow
from PyQt5.QtTest import QTest
import unittest
import threading
import time

class TestAppStartCorrectly(unittest.TestCase):
    """this test will check if no exceptions are thrown while gui launching.
    It tests also if a SystemExit is called (true, in fact a thread will be spawned
    to close the GUI). 
    Other types of exceptions will cause the test's failure.
    """

    def close_gui_operation(self, seconds_of_sleep):
        time.sleep(seconds_of_sleep)
        self.app.close()

    def start_closing_gui(self):
        self.thread.start()
    
    def build_app(self):
        self.app = TestApplicationWindow()
    
    def spawn_thread_to_close_app_after_seconds(self, seconds):
        self.thread = threading.Thread(target=self.close_gui_operation, args=(seconds,))

    def run_gui(self):
        self.app.run()

    def test_callbacks_are_triggered_by_event(self):
        with self.assertRaises(SystemExit):
            self.build_app()
            self.spawn_thread_to_close_app_after_seconds(0.1)
            self.start_closing_gui()
            self.run_gui()

if __name__ == '__main__':
    unittest.main()