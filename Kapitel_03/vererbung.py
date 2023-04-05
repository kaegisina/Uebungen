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
    
    def __str__(self):
        return f"Kreis Mittelpunkt = {self.mittelpunkt}, r = {self.radius}"


M = Punkt(2,3)
k1 = Kreis(M,10)
k2 = Kreis (Punkt(2,3), 10) #k1 und k2 ist dasselbe

print(k1)
print(k1.flaeche())

M.x = 5
print(k1)

k1.mittelpunkt.x = -5
print(M)