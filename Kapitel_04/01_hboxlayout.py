import sys
from PyQt5.QtWidgets import *  #Um Widget Fenster machen

class Fenster(QMainWindow):
    def __init__(self):
        super().__init__()

        # Fenster-Titel definieren:
        self.setWindowTitle("QHBoxLayout Demo")

        # Layout erstellen:
        layout = QHBoxLayout()  #H für Horizontale Anordnung von Buttons, V für vertikale Anordnung von Buttons

        # 3 Push-Buttons erzeugen:
        button1 = QPushButton("Hello")
        button2 = QPushButton("PyQt5")
        button3 = QPushButton("World")
        label = QLabel("Hello World")
        lineedit = QLineEdit()
        calendar = QCalendarWidget()

        # Buttons dem Layout hinzufügen
        layout.addWidget(button1)
        layout.addWidget(button2)
        layout.addWidget(button3)
        layout.addWidget(label)
        layout.addWidget(lineedit)
        layout.addWidget(calendar)

        # Zentrales Widget erstellen und layout hinzufügen
        center = QWidget()
        center.setLayout(layout)

        # Zentrales Widget in diesem Fenster setzen
        self.setCentralWidget(center)

        # Fenster anzeigen
        self.show()

def main():
    app = QApplication(sys.argv)  # Qt Applikation erstellen
    mainwindow = Fenster()       # Instanz Fenster erstellen
    mainwindow.raise_()           # Fenster nach vorne bringen
    app.exec_()                   # Applikations-Loop starten, das Programm läuft weiter und wird nicht gestoppt

if __name__ == '__main__':
    main()