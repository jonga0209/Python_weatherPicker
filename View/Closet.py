# -*- coding: utf-8 -*-

import sys

import PyQt5
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import uic

closetUi = '../_uiFile/viewCloset.ui'

class ClosetDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self, None)
        uic.loadUi(closetUi, self)


if __name__ == "__main__" :
    app = QApplication(sys.argv)
    main_dialog = ClosetDialog()
    main_dialog.show()
    app.exec_()