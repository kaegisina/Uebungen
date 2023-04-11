#Erweitern Sie das GUI der letzten Aufgaben um folgendes:
#a)	Verändern Sie das Verhalten bei "Speichern": 
#•	Es soll ein Filedialog verwendet werden um die Datei zu speichern.
#b)	Mit dem Button "Auf Karte zeigen" oder über das Menu "View/Karte..." wird ein Webbrowser mit Google Maps geöffnet. Der Link kann mithilfe der Adresse zusammengesetzt werden, z.B:
#c)	Fügen Sie den Button "Laden" hinzu. Dieser lädt einen zuvor gespeicherten Datensatz und stellt die Daten im GUI dar. 
#•	Verwenden Sie dazu einen File-Dialog.
#•	Fügen Sie auch einen Menu-Eintrag zum Laden des Datensatzes hinzu.
 

import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import*

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("GUI - Programierung")

        #layout erzeugen
        #layout = ... # QVBoxLayout(), QHBoxLayout(), QGridlayout(), QFormLayout()...
        layout = QFormLayout()

        #gui Elemente erstellen------------------------------------------------
        self.Vorname = QLineEdit()
        self.Name = QLineEdit()
        self.Geburtstag = QDateEdit()
        self.Adresse = QLineEdit()
        self.Postleitzahl = QLineEdit()
        self.Ort = QLineEdit()
        self.Land = QComboBox()
        self.Button = QPushButton("Save")
        self.button1 = QPushButton("Auf Karte zeigen")
        self.button2 = QPushButton("Laden")
        self.Land.addItems(["Schweiz", "Deutschland", "Österreich"])
    

        #gui Elemente dem Layout hinzufügen------------------------------------
        layout.addRow("Vorname:", self.Vorname)
        layout.addRow("Name:", self.Name)
        layout.addRow("Geburtstag:", self.Geburtstag)
        layout.addRow("Adresse:", self.Adresse)
        layout.addRow("Postleizahl:", self.Postleitzahl)
        layout.addRow("Ort:", self.Ort)
        layout.addRow("Land:", self.Land)
        layout.addRow(self.button1)
        layout.addRow(self.button2)
        layout.addRow(self.Button)

        #Menubar:--------------------------------------------------------------
        menubar = self.menuBar()
        file = menubar.addMenu("File")
        view = menubar.addMenu("View")

        self.save = QAction("Save", self)
        self.quit = QAction("Quit", self)
        self.kartee = QAction("Karte", self)
        self.ladenn = QAction("Laden", self)

        file.addAction(self.save)
        file.addAction(self.quit)
        view.addAction(self.kartee)
        file.addAction(self.ladenn) 

        # Button Connection----------------------------------------------------     
        self.Button.clicked.connect(self.textFile)
        self.save.triggered.connect(self.textFile)
        self.quit.triggered.connect(self.close)
        self.kartee.triggered.connect(self.karte)
        self.ladenn.triggered.connect(self.laden)
        self.button1.clicked.connect(self.karte)
        self.button2.clicked.connect(self.laden)

        center = QWidget()
        center.setLayout(layout)

        self.setCentralWidget(center)

        self.show()

    # Text File:----------------------------------------------------------------    
    def textFile(self):
        filename, filter = QFileDialog.getSaveFileName(self, "Datei speichern", "", "Text Datei (*.txt)")
        g = self.Geburtstag.date().toString("dd.MM.yyyy") # .date().toString("dd.MM.yyyy") um das format zu definieren
        text = f"{self.Vorname.text()},{self.Name.text()},{g},{self.Adresse.text()},{self.Postleitzahl.text()},{self.Ort.text()},{self.Land.currentText()}"
        file = open(filename, "w",encoding = "utf-8")  
        file.write(text)
    
    def close(self):
        self.close()

    #--------------------------------------------------------------------------

    def karte (self):
        import urllib.parse
        query = "Hello World"
        a = urllib.parse.quote(query)
        link = f"https://www.google.ch/maps/place/{self.Adresse.text()}+{self.Postleitzahl.text()}+{self.Ort.text()}+{self.Land.currentText()}"
        QDesktopServices.openUrl(QUrl(link))

    def laden (self):
        filename, filter = QFileDialog.getOpenFileName(self, "Datei öffnen", "", "Text Datei(*.txt)")
        if filename:
            with open(filename, "r",encoding = "utf-8") as f:
                data = f.read()
        fields = data.split(",")

        self.Vorname.setText(fields[0])
        self.Name.setText(fields[1])
        date = QDate.fromString(fields[2], "dd.MM.yyyy")
        self.Geburtstag.setDate(date)
        self.Adresse.setText(fields[3])
        self.Postleitzahl.setText(fields[4])
        self.Ort.setText(fields[5])  
        self.Land.setCurrentText(fields[6])





    

def main():
    app = QApplication(sys.argv)  # Qt Applikation erstellen
    mainwindow = MyWindow()       # Instanz Fenster erstellen
    mainwindow.raise_()           # Fenster nach vorne bringen
    app.exec_()                   # Applikations-Loop starten

if __name__ == '__main__':
    main()