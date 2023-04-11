from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Fenster(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Layout")

        layout =QVBoxLayout()

        button1 = QPushButton("Info")
        button2 = QPushButton("About")
        button3 = QPushButton("Warning")
        button4 = QPushButton("Frage")
        button5 = QPushButton("Load")
        button6 = QPushButton("Save")
        button7 = QPushButton("Zahl")
        button8 = QPushButton("Auswahl")
        button9 = QPushButton("Text")
        button0 = QPushButton("Weiteres")

        layout.addWidget(button1)
        layout.addWidget(button2)
        layout.addWidget(button3)
        layout.addWidget(button4)
        layout.addWidget(button5)
        layout.addWidget(button6)
        layout.addWidget(button7)
        layout.addWidget(button8)
        layout.addWidget(button9)
        layout.addWidget(button0)

        button1.clicked.connect(self.info)
        button2.clicked.connect(self.about)
        button3.clicked.connect(self.warn)
        button4.clicked.connect(self.question)
        button5.clicked.connect(self.load)
        button6.clicked.connect(self.save)
        button7.clicked.connect(self.zahl)
        button8.clicked.connect(self.auswahl)
        button9.clicked.connect(self.texteingabe)
        button0.clicked.connect(self.weiteres)

        center = QWidget()
        center.setLayout(layout)

        self.setCentralWidget(center)

        self.show()

    def info (self):
        QMessageBox.information(self,"Titel","Text\nzweitezeile")

    def about(self):
        QMessageBox.about(self, "Titel", "Dies ist eine weitere Info")  #Bei .about kommt das i nicht

    def warn (self):
        QMessageBox.warning(self, "Titel" , "Das File kann nicht gespeichert werden")

    def question(self):
        antwort = QMessageBox.question(self, "Frage", "Ist heute schönes Wetter?", QMessageBox.Yes, QMessageBox.No)
        if antwort == QMessageBox.Yes:
            QMessageBox.about(self, "Antwort", "Sehr gut. Es ist schön wenn das Wetter schön ist.")
        else:
            QMessageBox.about(self, "Antwort", "Schade")

    def load(self):
        filename, filter = QFileDialog.getOpenFileName(self, "Datei öffnen", "", "Text Files (*.txt)")  #Man kann hier jedes File eingeben, zum zwei: erstes ;; zweites , das zweite "" immer leer lassen, sonst wird unterordner gemacht
        
        if filename != "":
            print(filename)
        else:
            print("Abgebrochen")

    def save(self):
        filename, filter = QFileDialog.getSaveFileName(self, "Datei speichern", "", "Text Datei (*.txt)")

    def zahl(self):
        zahl, ok = QInputDialog.getInt(self, "Titel", "Geben sie eine Zahl an", 10, 5, 15) #Zahlen: Startwert, Minimalwert, Maximalwert
        if ok:
            if zahl ==12:
                print("Richtig geraten!!")
            else:
                print("Leider falsch")
        else:
            print("abgebrochen")
    
    def auswahl(self):
        farbe, ok = QInputDialog.getItem(self, "Auswahl", "Was ist ihre Lieblingsfarbe?",["rot", "grün", "gelb", "blau"], 1, True)

        if ok:
            print(farbe)

    def texteingabe(self):
        text, ok = QInputDialog.getText(self, "Titel", "Bitte Text eingeben", QLineEdit.Password, "") #Anstatt Passwort -> .Normal um einen normalen Text einzugeben
        if ok:
            print(text)

    def weiteres(self):
        color = QColorDialog.getColor()
        print(color.red(), color.green(), color.blue())
        font = QFontDialog.getFont()


app = QApplication([])
win = Fenster()
app.exec()