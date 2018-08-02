import sys

from PyQt5 import QtWidgets
from core import Ui_Dialog

class ApplicationWindow(QtWidgets.QWidget):
    def __init__(self):
        super(ApplicationWindow, self).__init__()

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    sys.exit(app.exec_())
