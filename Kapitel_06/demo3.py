from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import *

class UIFenster(QMainWindow):
    def __init__ (self):
        super(). __init__()
        loadUi("Kapitel_06/demo.ui", self)
        self.show()

        self.helloButton.clicked.connect(self.buttonclick)

    def buttonclick(self):
        print("Hello2")
        

app = QApplication([])
wind = UIFenster()
app.exec()
