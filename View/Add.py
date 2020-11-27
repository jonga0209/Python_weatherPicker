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
        self.a_img_clothes1.setStyleSheet('image:url(../image/cardigan.png);')
        self.a_img_clothes2.setStyleSheet('image:url(../image/coat.png);')
        self.a_img_clothes3.setStyleSheet('image:url(../image/fleece.png);')
        self.a_img_clothes4.setStyleSheet('image:url(../image/hoodzip_up.png);')
        self.a_img_clothes5.setStyleSheet('image:url(../image/jacket.png);')
        self.a_img_clothes6.setStyleSheet('image:url(../image/padding.png);')
        self.a_img_tem.setStyleSheet('image:url(../image/tem.png);')

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    main_dialog = AddDialog()
    main_dialog.show()
    app.exec_()