# -*- coding: utf-8 -*-

import sys

import PyQt5
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import uic

addUi = '../_uiFile/viewAdd.ui'

class AddDialog(QDialog):

    #전역변수 사용시 self.season 처럼 사용
    name = ''
    season = ''
    tem = ''
    clothes = ''

    def setSeason(self, s):
        self.season = s

    def setTem(self, t):
        self.tem = t

    def setClothes(self,c):
        self.clothes = c

    def __init__(self):
        QDialog.__init__(self, None)
        uic.loadUi(addUi, self)

        self.name = '-'
        self.season = '-'
        self.tem = '-'
        self.clothes = '-'

        # 이미지 셋팅
        self.a_img_clothes1.setStyleSheet('image:url(../image/cardigan.png);')
        self.a_img_clothes2.setStyleSheet('image:url(../image/coat.png);')
        self.a_img_clothes3.setStyleSheet('image:url(../image/fleece.png);')
        self.a_img_clothes4.setStyleSheet('image:url(../image/hoodzip_up.png);')
        self.a_img_clothes5.setStyleSheet('image:url(../image/jacket.png);')
        self.a_img_clothes6.setStyleSheet('image:url(../image/padding.png);')
        self.a_img_tem.setStyleSheet('image:url(../image/tem.png);')

        #btn_리스너
        self.a_btn_add.clicked.connect(self.btn_add)

        #btn_radio season
        self.a_rb_s_spring.clicked.connect(self.groupBox_season)
        self.a_rb_s_summer.clicked.connect(self.groupBox_season)
        self.a_rb_s_fall.clicked.connect(self.groupBox_season)
        self.a_rb_s_winter.clicked.connect(self.groupBox_season)

        # btn_radio tem
        self.a_rb_t00.clicked.connect(self.groupBox_tem)
        self.a_rb_t05.clicked.connect(self.groupBox_tem)
        self.a_rb_t10.clicked.connect(self.groupBox_tem)
        self.a_rb_t13.clicked.connect(self.groupBox_tem)
        self.a_rb_t16.clicked.connect(self.groupBox_tem)
        self.a_rb_t20.clicked.connect(self.groupBox_tem)

        # btn_radio tem
        self.a_rb_clothes1.clicked.connect(self.groupBox_clothes)
        self.a_rb_clothes2.clicked.connect(self.groupBox_clothes)
        self.a_rb_clothes3.clicked.connect(self.groupBox_clothes)
        self.a_rb_clothes4.clicked.connect(self.groupBox_clothes)
        self.a_rb_clothes5.clicked.connect(self.groupBox_clothes)
        self.a_rb_clothes6.clicked.connect(self.groupBox_clothes)

    def groupBox_season(self):
        if self.a_rb_s_spring.isChecked():
            self.setSeason('spring')
        elif self.a_rb_s_summer.isChecked():
            self.setSeason('summer')
        elif self.a_rb_s_fall.isChecked():
            self.setSeason('fall')
        elif self.a_rb_s_winter.isChecked():
            self.setSeason('winter')

    def groupBox_tem(self):
        if self.a_rb_clothes1.isChecked():
            self.setTem('00')
        elif self.a_rb_clothes2.isChecked():
            self.setTem('05')
        elif self.a_rb_clothes3.isChecked():
            self.setTem('10')
        elif self.a_rb_clothes4.isChecked():
            self.setTem('13')
        elif self.a_rb_clothes5.isChecked():
            self.setTem('16')
        elif self.a_rb_clothes6.isChecked():
            self.setTem('20')

    def groupBox_clothes(self):
        if self.a_rb_clothes1.isChecked():
            self.setClothes('1')
        elif self.a_rb_clothes2.isChecked():
            self.setClothes('2')
        elif self.a_rb_clothes3.isChecked():
            self.setClothes('3')
        elif self.a_rb_clothes4.isChecked():
            self.setClothes('4')
        elif self.a_rb_clothes5.isChecked():
            self.setClothes('5')
        elif self.a_rb_clothes6.isChecked():
            self.setClothes('6')

    def btn_add(self):
        if(self.a_te_name != ''):
            self.name = self.a_te_name.toPlainText()

        self.fileWrite(self.name, self.season, self.tem, self.clothes)

        # 입력 확인은 처음에 init에서 모든 변수를 '-'를 기본으로 설정한 것을 바탕으로 해서 해결
        # if self.name, self.season, self.tem, self.clothes != '-':
        #     self.fileWrite(self.name, self.season, self.tem, self.clothes)
        #     print('입력!')
        # else:
        #     print('잘못입력!')

    def fileWrite(self, n,s,t, c):
        f = open("C:/Users/user/Python/Python_weatherPicker/File/fileTest.txt", 'a', encoding='UTF-8')
        f.write(n + '/' + s + '/' + t +'/'+ c +'\n')
        f.close()

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    main_dialog = AddDialog()
    main_dialog.show()
    main_dialog.exec_()
