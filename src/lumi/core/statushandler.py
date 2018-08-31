
from lumi.core.observer import Observer

class StatusHandler(Observer):
    _statuses = []

    def push(self, status):
        self._statuses.append(status)
        self.on_pushed_status(status)
    
    def pop(self):
        return self._statuses.pop()

    def on_pushed_status(self, status):
        pass
