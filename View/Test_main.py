from View.Main import MainDialog
from PyQt5.QtWidgets import *
import sys
from PyQt5 import uic

app = QApplication(sys.argv)
main_dialog = MainDialog()
main_dialog.show()
sys.exit(app.exec_())