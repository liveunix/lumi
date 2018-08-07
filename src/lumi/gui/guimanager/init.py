import sys

from PyQt5 import QtWidgets
from guimanager.core import Ui_Dialog
from guimanager.eventhandler import GUIEventHandler

class ApplicationWindow(QtWidgets.QWidget, Ui_Dialog, GUIEventHandler):
    
    def __init__(self):
        super(ApplicationWindow, self).__init__()

        self.setup_ui_dialog()  
        for index, tabname in enumerate(['tab', 'tabddd']):
            self.setup_tab_structure_with_index_and_name(index, tabname)
        self.set_buddies()   
        self.retranslate_ui_dialog()

        self.route_callbacks_to_objects()

def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    sys.exit(app.exec_())
