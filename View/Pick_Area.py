# -*- coding: utf-8 -*-

import sys

import PyQt5
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
from data.weather import Weather
from data.date import Date

# from typing import TYPE_CHECKING
# if TYPE_CHECKING:

from View.Closet import ClosetDialog

mainUi = '../_uiFile/viewStart.ui'

class MainDialog(QDialog):
    def __init__(self):
        super(MainDialog, self).__init__()
        QDialog.__init__(self, None)
        uic.loadUi(mainUi, self)
        #날씨
        self.weather = Weather()
        self.weather.getWeather()

        #클릭
        self.m_btn_seoul.clicked.connect(lambda state,button = self.m_btn_seoul: self.click_area(state,button))
        self.m_btn_busan.clicked.connect(lambda state,button = self.m_btn_busan: self.click_area(state,button))
        self.m_btn_dejun.clicked.connect(lambda state,button = self.m_btn_dejun: self.click_area(state,button))
        self.m_btn_jeju.clicked.connect(lambda state,button = self.m_btn_jeju: self.click_area(state,button))
        self.m_btn_ham.clicked.connect(lambda state,button = self.m_btn_ham: self.click_area(state,button))

        self.draw_ui()



    def click_area(self,state ,button):
        self.weather.setLocation(button.text())
        self.weather.getWeather()
        self.m_la_tem.setText(self.weather.getTemperature()+'°C')
        self.m_la_state.setText(self.weather.getComment())





if __name__ == "__main__" :
    # QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)
    main_dialog = MainDialog()
    # 프로그램 화면을 보여주는 코드
    main_dialog.show()
    # 프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()