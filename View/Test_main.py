from View.Main import MainDialog
from PyQt5.QtWidgets import *
import sys
from PyQt5 import uic

app = QApplication(sys.argv)
main_dialog = MainDialog()
# 프로그램 화면을 보여주는 코드
main_dialog.show()
# 프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
app.exec_()