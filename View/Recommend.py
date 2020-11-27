# -*- coding: utf-8 -*-

import sys

import PyQt5
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import uic

recommendUi = '../_uiFile/viewRecommend.ui'

class RecommendDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self, None)
        uic.loadUi(recommendUi, self)
        self.r_img_clothes1.setStyleSheet('image:url(../image/coat.png);')
        self.show()
        self.exec_()


if __name__ == "__main__" :
    app = QApplication(sys.argv)
    main_dialog = RecommendDialog()
    main_dialog.show()
    sys.exit(app.exec_())
