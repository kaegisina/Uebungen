from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import *
from PyQt5.QtGui import*
import urllib.parse

class UIFenster(QMainWindow):
    def __init__ (self):
        super(). __init__()
        loadUi("Kapitel_06/showmap.ui", self)
        self.show()
        self.pushButton.clicked.connect(self.buttonclick)

    def buttonclick(self):
        self.breite = self.lineEdit.text()
        self.laenge = self.lineEdit_2.text()
        query = "Hello World"
        a = urllib.parse.quote(query)
        link = f"https://www.google.ch/maps/place/{self.breite},{self.laenge}"
        QDesktopServices.openUrl(QUrl(link))
        

app = QApplication([])
wind = UIFenster()
app.exec()