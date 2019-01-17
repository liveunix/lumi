from lumi.gui.guimanager.core import ApplicationWindow


class TestApplicationWindow(ApplicationWindow):
    def show(self):
        """Main ApplicationWindow class will call the show() method to render the window,
           this is the test version of the ApplicationWindow class so we don't need to show the GUI:
           overriding this method the rendering will be avoided."""
        pass
