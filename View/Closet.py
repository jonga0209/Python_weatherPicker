# -*- coding: utf-8 -*-

import sys

import PyQt5
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import uic

from typing import TYPE_CHECKING



closetUi = '../_uiFile/viewCloset.ui'

class ClosetDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self, None)
        uic.loadUi(closetUi, self)
        # sys.exit(app.exec_())
        self.c_btn_main.clicked.connect(self.click_main)
        self.c_btn_add.clicked.connect(self.click_add)


    def click_main(self):
        from View.Main import MainDialog
        self.accept()
        r = MainDialog()
        r.show()
        r.exec_()

    def click_add(self):
        from View.Add import AddDialog
        self.accept()
        r = AddDialog()
        r.show()
        r.exec_()


if __name__ == "__main__" :
    app = QApplication(sys.argv)
    main_dialog = ClosetDialog()
    main_dialog.show()
    sys.exit(app.exec_())