import matplotlib.pyplot as plt
from math import sin, pi

x = []
y = []
for i in range(0, 101):
    value = i/(100/(4*pi))-2*pi
    x.append(value)
    y.append(sin(value))

plt.plot(x, y, "c--") #mit Doppelpunkt -> gestrichelte Linie, o -> dick, x -> anstatt Punkt Kreuz,  im Skript weitere
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.axis("equal")
plt.show()
