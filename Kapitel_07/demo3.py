import matplotlib.pyplot as plt
from math import sin, pi
import numpy as np

x = np.linspace(-np.pi, np.pi, 150)
y1= np.sin(x)
y2= np.cos(x)


plt.plot(x, y1, "k-") #mit Doppelpunkt -> gestrichelte Linie, o -> dick, x -> anstatt Punkt Kreuz,  im Skript weitere
plt.plot(x, y2,"b-")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Sinus und Cosinus")
plt.grid(True)
plt.axis("equal")
plt.show()
