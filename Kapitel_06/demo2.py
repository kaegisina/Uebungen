from PyQt5.QtWidgets import *
from PyQt5.uic import *

def clickbutton():
    print("Hello World")

app = QApplication([])

window = loadUi("Kapitel_06/demo.ui")
window.show()

window.helloButton.clicked.connect(clickbutton)

app.exec()