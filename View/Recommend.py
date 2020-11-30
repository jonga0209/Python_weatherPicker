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
        self.r_btn_main.clicked.connect(self.click_main)
        self.r_btn_closet.clicked.connect(self.click_closet)

        self.draw_ui()


    def draw_ui(self):
        from data.date import Date
        from data.weather import Weather
        date = Date()
        weather = Weather()
        self.r_la_year.setText(str(date.getYear()))
        self.r_la_day.setText(date.__str__())
        self.r_la_tem.setText(str(weather.getTemperature())+'℃')

    def click_main(self):
        from View.Main import MainDialog
        self.accept()
        r = MainDialog()
        r.show()
        r.exec_()

    def click_closet(self):
        from View.Closet import ClosetDialog
        self.accept()
        r = ClosetDialog()
        r.show()
        r.exec_()


if __name__ == "__main__" :
    app = QApplication(sys.argv)
    main_dialog = RecommendDialog()
    main_dialog.show()
    # 프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()

