import numpy as np

a = np.array([1,2,3,4], dtype=np.float64)

b = np.array([[1,2,3], [4,5,6], [7,8,9]])

if 5 in b:
    print("5 kommt in der Matrix b vor!")
else:
    print("Schade")


print(b[1,:]) #2. Zeile der Matrix ausgeben
print(b[:,0]) #1. Spalte der Matrix ausgeben

c= np.zeros([4,4]) #Nullmatrix 4x4
c[0,1] = 5 #Werte zuweisen
print(c)

d = np.arange(1, 100, 2) #das gleiche wie Range früher Start, Ende, Schritte
print(d)


e = np.arange(-2*np.pi, 2*np.pi, 0.1) 
print(e)

f = np.linspace(0,1,1000)
print(np.sin(f))

g = np.random.random(20) #20 zufällige Werte zwischen 0 und 1
print(g)