import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.createLayout()
        self.createConnects()

    def createLayout(self):
        # Fenster-Titel definieren:
        self.setWindowTitle("Widget Inhalt lesen")

        # Layout erstellen:
        layout = QFormLayout()

        # Widget-Instanzen erstellen:

        self.nameLineEdit = QLineEdit()
        self.zahlLineEdit = QLineEdit()
        self.button = QPushButton("Auswerten")
        self.a = QLineEdit()
        self.b = QLineEdit()

        # Layout füllen:
        layout.addRow("Name:", self.nameLineEdit)
        layout.addRow("Zahl:", self.zahlLineEdit)
        layout.addRow("a:", self.a)
        layout.addRow("b:", self.b)
        layout.addRow(self.button)

        # Zentrales Widget erstellen und layout hinzufügen
        center = QWidget()
        center.setLayout(layout)

        # Zentrales Widget in diesem Fenster setzen
        self.setCentralWidget(center)

        # Fenster anzeigen
        self.show()

    #connects
    def createConnects(self):
        self.button.clicked.connect(self.auswertung)

    def auswertung(self):
        name = self.nameLineEdit.text()
        print("Der Name ist", name)
        try:
            zahl = float(self.zahlLineEdit.text())
            print("Die Zahl ist:", zahl)
            print("Zahl * 2 = ", zahl*2)
        except ValueError:
            print("keine gültige Zahl eingegeben!!")

        werta = float(self.a.text())
        wertb = float(self.b.text())

        print(werta + wertb)

def main():
    app = QApplication(sys.argv)  # Qt Applikation erstellen
    mainwindow = MyWindow()       # Instanz Fenster erstellen
    mainwindow.raise_()           # Fenster nach vorne bringen
    app.exec_()                   # Applikations-Loop starten

if __name__ == '__main__':
    main()