import matplotlib.pyplot as plt
from math import sin, pi
import numpy as np

x = np.linspace(-np.pi, np.pi, 150)
y1= np.sin(x)
y2= np.cos(x)

fig, ax = plt.subplots(2) #Wenn man in Klammer ein 2,2 schreibt ist ein 2x2 Plot
ax[0].plot(x, y1, "k-") #mit Doppelpunkt -> gestrichelte Linie, o -> dick, x -> anstatt Punkt Kreuz,  im Skript weitere
ax[1].plot(x, y2,"b-")

plt.show()
