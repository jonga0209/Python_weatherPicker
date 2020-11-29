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
        self.img = ['','image:url(../image/cardigan.png);','image:url(../image/coat.png);','image:url(../image/fleece.png);','image:url(../image/hoodzip_up.png);'
           ,'image:url(../image/jacket.png);','image:url(../image/padding.png);','image:url(../image/tem.png);']
        self.clothes_labeles = []
        self.name_labeles = []
        self.season_labeles = []
        self.temperature_labeles =[]
        # for i in range(0,4):
        #     label = QLabel("a",self)
        #     label.setGeometry(20+i*320,170,171,211)
        #     label.setStyleSheet('background-color: rgb(217, 197, 255)')
        #     self.clothes_label.append(label)

       # self.groupBox_1.hide()
        self.c_btn_main.clicked.connect(self.click_main)
        self.c_btn_add.clicked.connect(self.click_add)
        self.file_read()

    def file_read(self):
        f = open('../File/userClothesInfo.txt','r', encoding='UTF-8')
        try:
            lines = f.readlines()
            self.draw_ui(lines)
        except FileNotFoundError as e:
            print(e)
        finally:
            f.close()

    def draw_ui(self,lines):
        j = 0
        for i in range(0,len(lines)):
            line = lines[i].split('/')
            if line[0] == '\n': # 혹시나 txt파일 건든후 마지막 줄 만들기xx(\n) 예외처리
                break;

            name = line[0]
            season = line[1]
            temperature = line[2]
            clothes = line[3]

            if i>3:j=1
            i = i%4

            #옷
            img_clothes = QLabel('',self)
            img_clothes.setStyleSheet(self.img[int(clothes)])
            img_clothes.setGeometry(20+i*320,170+300*j,171,211)
            #img_clothes.setStyleSheet('background-color: rgb(217, 197, 255)')
            self.clothes_labeles.append(img_clothes)

            #이름
            label_name = QLabel(name, self)
            label_name.setAlignment(Qt.AlignCenter)
            label_name.setGeometry(20 + i * 320, 370+300*j, 171, 51)
            label_name.setStyleSheet('background-color: rgb(144, 216, 255)')
            self.name_labeles.append(label_name)

            #계절
            label_season = QLabel(season, self)
            label_season.setGeometry(200 + i * 320, 170+300*j, 121, 61)
            label_season.setStyleSheet('background-color: rgb(144, 216, 255)')
            self.name_labeles.append(label_season)

            #온도
            label_temperature = QLabel(temperature, self)
            label_temperature.setGeometry(200 + i * 320, 240+300*j, 121, 61)
            label_temperature.setStyleSheet('background-color: rgb(144, 216, 255)')
            self.name_labeles.append(label_temperature)


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