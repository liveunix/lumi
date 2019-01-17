from lumi.core.observer import Observer
from io import StringIO
import sys


class StatusHandler(Observer):
    _statuses = []
    buf = None

    def push(self, status):
        self._statuses.append(status)
        self.on_pushed_status(status)

    def pop(self):
        return self._statuses.pop()

    def on_pushed_status(self, status):
        pass

    def buf():
        return buf

    def write_to_stdout():
        buf = StringIO()
        sys.stdout = buf
