#Aufgabe 1: Magische Methoden
#Implementieren Sie eine Klasse Vector3, welche einen 3D Vektor repräsentiert.
#Dabei sollen Magische Methoden implementiert werden:
#• Konversion zu Zeichenkette
#• Addition
#• Subtraktion
#• komponentenweise Multiplikation (Vector3 * Vector3)
#• Multiplikation mit Skalar (float * Vector3) oder (int * Vector3) oder (Vector3 * float) oder (Vector3 * int)

#Implementieren sie zudem auch folgende Methoden
#cross(b) Berechnung des Kreuzproduktes
#dot(b) Berechnung des Skalarprodukes
#normalize() Vektor normalisieren
import math

class Vector3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y 
        self.z = z

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"
    
    def __add__(self, other):
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self,other):
        return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def __mul__(self, other):
        if isinstance(other, Vector3):
            return Vector3(self.x * other.x, self.y * other.y, self.z * other.z)
        elif isinstance(other, (int, float)):
            return Vector3(self.x * other, self.y * other, self.z * other)
        
    def __rmul__(self,other):
        if isinstance(other, Vector3):
            return Vector3(self.x * other.x, self.y * other.y, self.z * other.z)
        elif isinstance(other, (int, float)):
            return Vector3(self.x * other, self.y * other, self.z * other)    

    def dot(self,other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross(self,other):
        return (self.y*other.z - self.z*other.y), (self.z*other.x - self.x*other.z), (self.x*other.y - self.y*other.x)

    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def normalize(self):
        magnitude = self.magnitude()
        if magnitude == 0:
            return self
        return Vector3(self.x/magnitude, self.y/magnitude, self.z/magnitude)

    
v1 = Vector3(3,4,2) 
v2 = Vector3(2,1,0)

# für __add__
v3 = v1 + v2
print(v3)

# für __sub__
v4 = v1 - v2
print(v4)

# für __mul__  /  Komponentenweise Multiplikation  /  Multiplikation mit Skalar und Float und Integer
c = v1 * v2
print(c)
h = 2.2 * v1
print(h)

# für skalarprodukt
e = v1.dot(v2) 
print(e)

# für kreuzprodukt
f = v1.cross(v2) 
print(f)

# für normalize
normalized_vector = v1.normalize()
print(normalized_vector)



a = 12.5 # a = 5 # a = Vector3(23,4,2)
if type(v1) == Vector3:
    print("v1 ist eine Vektor3-Klasse")
if type(v1) == float:
    print("v1 ist ein float")
if type(v1) == int:
    print("v1 ist ein Integer")


#Musterlösung:
class Vector3:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y 
        self.z = z

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"
    
    def __add__(self, other):
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self,other):
        return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)
    
    #das hat sich bisschen geändert in Musterlösung
    def __mul__(self, other):
        if type(other) == Vector3:
            return Vector3(self.x * other.x, self.y * other.y, self.z * other.z)
        elif type(other) == float or type(other) == int:
            return Vector3(self.x * other, self.y * other, self.z * other)
    
    #das auch
    def __rmul__(self,other):
        return Vector3(self.x * other.x, self.y * other.y, self.z * other.z)

    def dot(self,other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross(self, other):
        return (self.y*other.z - self.z*other.y), (self.z*other.x - self.x*other.z), (self.x*other.y - self.y*other.x)
    
    #das auch
    def magnitude(self):
        return (self.x**2 + self.y**2 + self.z**2)**0.5


    def normalize(self):
        r = self.magnitude()
        return Vector3(self.x / r, self.y / r, self.z / r)


