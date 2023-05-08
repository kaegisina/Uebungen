from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import numpy as np

class Window (QMainWindow):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        figure = plt.figure(figsize = (16,9))
        self.canvas = FigureCanvas(figure)

        self.x = QLineEdit("np.linspace(-2*np.pi,2*np.pi)")
        self.y = QLineEdit("np.sin(x)")

        button = QPushButton("Plot")

        layout.addWidget(self.canvas)
        layout.addWidget(self.x)
        layout.addWidget(self.y)
        layout.addWidget(button)

        center = QWidget()
        center.setLayout(layout)

        self.setCentralWidget(center)
        self.show()

        button.clicked.connect(self.plot)
    
    def plot(self):
        plt.clf()
        xx = self.x.text()
        yy = self.y.text()
        try:
            x = eval(xx)
            y = eval(yy)
        except:
            QMessageBox.critical(self, "Fehler", "x und y bitte korrekt eingeben")
            return
        try:
            plt.plot(x, y, "ko-")
            plt.axis("equal")
            self.canvas.draw()
        except:
            QMessageBox.critical(self, "Fehler", "Bitte Eingabe überprüfen")
        
       

app = QApplication([])
window = Window()
app.exec()