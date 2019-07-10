from ui_SAMG_2 import *
#
import sys
from PySide2 import (QtCore, QtWidgets, QtGui)
from SAMG import *
from PySide2.QtWidgets import QPushButton
import random

class Ui_MainDialog(object):
    def ok(self):
        self.window=QtWidgets.QMainWindow
        self.ui=Ui_MainDialog()



class MainDialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_dialog = MainDialog()
    main_dialog.show()
    app.exec_()