import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        btn1 = QPushButton('옷장', self)
        btn1.move(1200, 50)
        btn2 = QPushButton('Button2', self)
        btn2.move(80, 53)

        self.setWindowTitle('Absolute Positioning')
        self.setGeometry(300, 50, 1300, 800)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())