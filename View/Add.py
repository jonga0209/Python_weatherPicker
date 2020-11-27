# -*- coding: utf-8 -*-

import sys

import PyQt5
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import uic

addUi = '../_uiFile/viewAdd.ui'

class AddDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self, None)
        uic.loadUi(addUi, self)


if __name__ == "__main__" :
    app = QApplication(sys.argv)
    main_dialog = AddDialog()
    main_dialog.show()
    app.exec_()