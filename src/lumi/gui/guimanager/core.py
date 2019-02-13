import sys

from PyQt5 import QtWidgets
from lumi.gui.guimanager.ui import Ui_Dialog
from lumi.gui.guimanager.eventhandler import GUIEventHandler
from lumi.gui.callbacks.callbacks_routing import ROUTING_OPTIONS

# some code is commented because there'is an implementation of the status handler mechanism
# using the Event triggering class that's not used yet
# from lumi.gui.guimanager.statushandler import GUIStatusHandler


class ApplicationWindow(QtWidgets.QWidget, Ui_Dialog, GUIEventHandler):
    def _construct_qapplication(self):
        self.app = QtWidgets.QApplication(sys.argv)

    def _setup_ui(self):
        self.setup_ui_dialog()
        for index, tabname in enumerate(["tab", "tabddd"]):
            self.setup_tab_structure_with_index_and_name(index, tabname)
        self.set_buddies()
        # self.retranslate_ui_dialog()

    """
    def _setup_gui_status_handler(self):
        self.gui_status_handler = GUIStatusHandler()
        self.gui_status_handler.observe(event_name='on_pushed_item', callback=self.gui_status_handler.on_pushed_item)
    """

    def __init__(self):
        self._construct_qapplication()
        super(ApplicationWindow, self).__init__()

        self._setup_ui()
        # self._setup_gui_status_handler()

        self.route_callbacks_to_objects(ROUTING_OPTIONS)

    def run(self):
        self.show()
        try:
            sys.exit(self.app.exec_())
        except SystemExit as e:
            pass
