# -*- coding: utf-8 -*-

import sys

import PyQt5
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import uic

recommendUi = '../_uiFile/viewRecommend.ui'

class RecommendDialog(QDialog):
    def __init__(self,parent):
        QDialog.__init__(self, None)
        uic.loadUi(recommendUi, self)


if __name__ == "__main__" :
    app = QApplication(sys.argv)
    main_dialog = RecommendDialog()
    main_dialog.show()
    app.exec_()