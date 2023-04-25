from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.uic import *


class UIFenster(QMainWindow):
    def __init__ (self):
        super(). __init__()
        loadUi("Kapitel_06/web.ui", self)
        self.show()

        self.pushButton.clicked.connect(self.buttonclick)

    def buttonclick(self):
        self.webEngineView.load(QUrl("https://www.fhnw.ch"))
        

app = QApplication([])
wind = UIFenster()
app.exec()