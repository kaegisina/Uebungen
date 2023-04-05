#Erstellen Sie eine Applikation mit folgendem GUI:
#a) Implementieren Sie das GUI wie abgebildet, wählen Sie ein geeignetes Layout
#b) Ein File-Menu mit den Einträgen Save und Quit soll hinzugefügt werden
#c) wird auf den Button "Save" gedrückt, so wird ein File output.txt angelegt, welches 
#die Daten kommagetrennt speichert, also für oberes Beispiel wäre der Inhalt:
#Bernhard,Müller,6/25/1986,Gründenstrasse 40,4132,Muttenz,Schweiz
#d) Beim Betätigen des "Quit" Menus wird das Programm beendet
#e) Beim Betätigen des "Save" Menus wird der Datensatz wie in c) gespeichert.
#Hinweis 1: Die QComboBox (Auswahl Land) kann folgendermassen erstellt werden:
#countries = QComboBox()
#countries.addItems(["Schweiz", "Deutschland", "Österreich"])

import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Fenster(QMainWindow):
    def __init__(self):
        super().__init__()

    def createLayout(self):
        self.setWindowTitle("GUI-Programmierung")

        #layout erzeugen
        layout = QFormLayout()

        #Widget-Instanzen erstellen:
        self.vornameLineEdit = QLineEdit()
        self.nachnameLineEdit = QLineEdit()
        self.geburtstag = QDateEdit()
        self.save = QPushButton("Save")
        self.adresseLineEdit = QLineEdit()
        self.plzLineEdit = QLineEdit()
        self.ortLineEdit = QLineEdit()
        self.landcombobox = QComboBox()
        self.landcombobox.addItems(["Schweiz", "Österreich", "Deutschland"])
     
        #gui Elemente dem Layout hinzufügen
        layout.addRow("Vorname:", self.vornameLineEdit)
        layout.addRow("Name:", self.nachnameLineEdit)
        layout.addRow("Geburtstag:", self.geburtstag)
        layout.addRow("Adresse:", self.adresseLineEdit)
        layout.addRow("Postleitzahl:", self.plzLineEdit)
        layout.addRow("Ort:", self.ortLineEdit)
        layout.addRow("Land:", self.landcombobox)
        layout.addRow(self.save)

        #file hinzufügen:
        menubar = self.menuBar()
        filemenu = menubar.addMenu("File")

        save = QAction("Save", self)
        save.triggered.connect(self.menu_save)
        quit = QAction("Quit", self)
        quit.triggered.connect(self.menu_quit)

        filemenu.addAction(save)
        filemenu.addAction(quit)


        center = QWidget()
        center.setLayout(layout)

        self.setCentralWidget(center)

        self.show()
    
    def createConnects(self):
        self.save.clicked.connect(self.menu_save)
    
    def speichern(self):
        file = open("Ausgabe.txt", "w", encoding ="utf-8")
        file.write(f"{self.vornameLineEdit.text()}, {self.nachnameLineEdit.text()}, {self.geburtstag.text()}, {self.adresseLineEdit.text()}, {self.plzLineEdit.text()}, {self.ortLineEdit.text()}, {self.landcombobox.currentText()}")
        file.close()



app = QApplication([])
win = Fenster()
app.exec()