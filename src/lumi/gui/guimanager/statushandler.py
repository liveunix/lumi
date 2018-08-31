from lumi.core.statushandler import StatusHandler

class GUIStatusHandler(StatusHandler):
    def __init__(self):
        StatusHandler.__init__(self)

    def on_pushed_status(self, data):
        # this function will be called whenever an item is pushed to status handler
        pass