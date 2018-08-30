from lumi.core.statushandler import StatusHandler

class Event:
    def __init__(self, name, data=None):
        self.name = name
        self.data = data

    def fire(self):
        for observer in StatusHandler._observers:
            if self.name in observer._observables:
                if self.data:
                    observer._observables[self.name](self.data)
                else:
                    observer._observables[self.name]
