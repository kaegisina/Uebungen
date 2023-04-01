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

    def __str__(self):
        return f"Punkt({self.x}, {self.y})"


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
  


class Rechteck(Figur):            
    def __init__(self, point1, point2):
        super().__init__("Rechteck")
        self.point1 = point1
        self.point2 = point2
        self.side1 = abs(point1.x - point2.x)  #Länge des Rechtecks
        self.side2 = abs(point1.y - point2.y)  #Breite des Rechtecks

    def umfang (self):
        return self.side1 * 2 + self.side2 *2 
    
    def __str__(self):
        return f"Rechteck Punkte = {self.point1}, {self.point2}, Länge = {self.side1}, Breite = {self.side2}"
    
class Polygon(Figur):            
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



#Kreis austesten
M = Punkt(2,3)
k1 = Kreis(M,10)

print(k1)
print(k1.flaeche())
print(k1.umfang())



#Rechteck austesten
D = (1,1)
E = (4,5)
r1 = Rechteck(D,E)
print(r1)
print(r1.umfang())

#Polygon austesten
