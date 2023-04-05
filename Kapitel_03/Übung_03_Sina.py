#Aufgabe 1: Vererbung
#Schreiben Sie die Klassen "Dreieck", "Rechteck", "Kreis" und "Polygon"
#Diese Klassen werden von folgender Python Klasse vererbt:
#class Figur:
#    def __init__(self):
#        self.name = "Figur"

#    def Umfang(self):
#        return 0
    
#    def __str__(self):
#        return self.name
    
#• Das Attribut "name" ist eine Zeichenkette welche den Namen des jeweiligen Objektes enthält.
#• Die Methode "Umfang" soll für die jeweilige Figur korrekt implementiert werden
#• Finden Sie geeignete Konstruktoren um die Figuren zu konstruieren
#• __str__ soll die Figur mit allen Koordinaten sinnvoll beschreiben, z.B:
#    o "Kreis M=(2.3,4.2) r=3.4"
#    o "Rechteck (0,0) – (10,15)"

#Hinweise:
#• Die Figuren sind 2D
#• Verwenden Sie eine Klasse Punkt („Point“) um die Koordinaten der Figuren zu verwalten.
#• Die Seiten bei Rechteck sind parallel zur jeweiligen Koordinaten-Achse.
#• Wählen Sie geeignete Konstruktoren, z.B. bei Polygon sollen beliebig viele Ecken unterstützt werden.

import math

class Figur:
    def __init__ (self, name):
        self.name = name

    def umfang (self):
        return 0     
    
    def flaeche (self):
        return 0
    
    def __str__ (self):
        return self.name


class Punkt(Figur):            #in Klammer Vererbung -> Punkt ist Vererbung von Figur
    def __init__(self, x, y):
        super().__init__("Punkt")
        self.x = x
        self.y = y 

    def distanz(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

    def __str__(self):
        return f"Punkt(x = {self.x}, y = {self.y})"


class Kreis(Figur):            #in Klammer Vererbung -> Kreis ist Vererbung von Figur
    def __init__(self, mittelpunkt, radius):
        super().__init__("Kreis")
        self.mittelpunkt = mittelpunkt
        self.radius = radius

    def flaeche (self):
        return self.radius**2 * math.pi
    
    def umfang (self):
        return self.radius*2 * math.pi
    
    def __str__(self):
        return f"Kreis Mittelpunkt = {self.mittelpunkt}, r = {self.radius}"
  
class Dreieck(Figur):            
    def __init__(self, A, B, C):
        super().__init__("Dreieck")
        self.A = A
        self.B = B
        self.C = C

    def umfang (self):
        return self.A.distanz(self.B) + self.B.distanz(self.C) + self.C.distanz(self.A)
    
    def __str__(self):
        return f"Dreieck Punkte = {self.A}, {self.B}, {self.C}"

class Rechteck(Figur):            
    def __init__(self, Pmin, Pmax):
        super().__init__("Rechteck")
        self.Pmin = Pmin
        self.Pmax = Pmax

    def umfang (self):
        return 2*abs(self.Pmax.x - self.Pmin.x) + 2*abs(self.Pmax.y - self.Pmin.y)
        
    
    def __str__(self):
        return f"Rechteck Punkte = {self.Pmin}, {self.Pmax}"
    

class Polygon(Figur):
    def __init__(self, Punktliste:
        super().__init__("Polygon")
        self.pl = Punktliste

    def umfang(self):
        s = 0
        for i in range (0, len(self.pl)-1):
            l1 = self.pl[i]
            l2 = self.pl[i+1]
            s = s + l1.distanz(l2)
        return s
        

    def __str__(self):
        s = f"Polygon: "
        for punkt in self.pl:
            s = s + f"{punkt}"
        return s
    



#Kreis austesten
M = Punkt(2,3)
k1 = Kreis(M,10)

print(k1)
print(k1.flaeche())
print(k1.umfang())

#Dreieck austesten
A = (-2,-2)
B = (3,-1)
C = (-1,3)
d1 = Dreieck(A,B,C)
print(d1)
print(d1.umfang())


#Rechteck austesten
D = (1,1)
E = (4,5)
r1 = Rechteck(D,E)
print(r1)
print(r1.umfang())


#Polygon austesten
polygonliste = [Punkt(1,1), Punkt(2,4), Punkt(3,3.4), Punkt(4,4), Punkt(4,1), Punkt(1,1)]

p1 = Polygon(polygonliste)
print(p1)
print(p1.umfang())