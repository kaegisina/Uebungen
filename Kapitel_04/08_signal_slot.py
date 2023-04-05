import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        ##########
        # LAYOUT #
        ##########

        # Fenster-Titel definieren:
        self.setWindowTitle("Signal Slot Demo")

        # Layout erstellen:
        layout = QVBoxLayout()

        # Widget-Instanzen erstellen:
        button1 = QPushButton("Button 1")
        button2 = QPushButton("Button 2")
        checkbox = QCheckBox("Python ist genial")
        checkbox.setCheckState(Qt.CheckState.Checked) #so ist Checkbox schon angewählt
        lineedit =QLineEdit()

        # Widgets dem Layout hinzufügen:
        layout.addWidget(button1)
        layout.addWidget(button2)
        layout.addWidget(checkbox)
        layout.addWidget(lineedit)

        # Zentrales Widget erstellen und layout hinzufügen
        center = QWidget()
        center.setLayout(layout)

        # Zentrales Widget in diesem Fenster setzen
        self.setCentralWidget(center)

        # Fenster anzeigen
        self.show()

        ############
        # CONNECTS #
        ############

        # Klick auf Button 1 ruft die Funktion button1_pressed() auf
        button1.clicked.connect(self.button1_clicked)

        # Klick auf Button 2 ruft die Funktion button1_pressed() auf, mit pressed anstatt clicked wird die Aktion schon ausgeführt bevor losgelassen wird
        button2.pressed.connect(self.button2_clicked)

        checkbox.stateChanged.connect(self.checkboxchanged)

        lineedit.textChanged.connect(self.text)


    def button1_clicked(self):
        print("Der Button 1 wurde gedrückt")

# Fenster wird geschlossen
    def button2_clicked(self):
        self.close()

#Checkbox
    def checkboxchanged(self,state):
        print("Checkbox bestätigt")
        if state == Qt.CheckState.Checked:
            print("ok ausgewählt")
        else:
            print("ok schade")

    def text(self, txt):
        print(txt)
        if txt == "quit":
            self.close()

def main():
    app = QApplication(sys.argv)  # Qt Applikation erstellen
    mainwindow = MyWindow()       # Instanz Fenster erstellen
    mainwindow.raise_()           # Fenster nach vorne bringen
    app.exec_()                   # Applikations-Loop starten

if __name__ == '__main__':
    main()