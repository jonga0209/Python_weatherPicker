# -*- coding: utf-8 -*-

import sys

import PyQt5
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
from data.weather import Weather
from data.date import Date
from View.Recommend import RecommendDialog
mainUi = '../_uiFile/viewMain.ui'

class MainDialog(QDialog):
    def __init__(self):
        super(MainDialog, self).__init__()
        QDialog.__init__(self, None)
        uic.loadUi(mainUi, self)
        #날씨
        self.weather = Weather()
        self.weather.getWeather()
        #날짜
        self.date = Date()
        #년도
        self.m_la_year.setText(str(self.date.getYear()))
        self.m_la_day.setText(self.date.__str__())
        #온도
        self.m_la_tem.setText(self.weather.getTemperature()+'°C')

        #클릭
        self.m_btn_reco.clicked.connect(self.btn_recommend)
        
        main_dialog.show()
        app.exec_()

    def btn_recommend(self):
        self.accept()
        r = RecommendDialog(self)
        print("클릭")


if __name__ == "__main__" :
    app = QApplication(sys.argv)
    main_dialog = MainDialog()
