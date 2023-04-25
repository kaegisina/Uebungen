from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import *

class UIFenster(QMainWindow):
    def __init__ (self):
        super(). __init__()
        loadUi("Kapitel_06/demo2.ui", self)
        self.show()

        self.Button.clicked.connect(self.buttonclick)

    def buttonclick(self):
        txt = self.lineEdit.text()
        print("Hello2", txt)
        

app = QApplication([])
wind = UIFenster()
app.exec()