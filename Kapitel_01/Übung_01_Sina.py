#Aufgabe 1
#Erstellen Sie eine Klasse Vector3, welche einen dreidimensionalen Vektor repräsentiert.
#Über den Konstruktor werden die Komponenten x, y und z definiert. Wird nichts angegeben, so wird ein Null-Vektor erstellt.
#Entwickeln Sie eine Methode len, welche die Länge des Vektors berechnet.
#Mit einer Instanz von Vector3 soll die Klasse getestet werden.

class Vector3:
    def __init__(self, x = None, y = None, z = None):
        self.x = x
        self.y = y
        self.z = z
        if x == None and y == None and z == None:
            self.x = 0
            self.y = 0
            self.z = 0

    def len (self):
        return( (self.x)**2 + 
            (self.y)**2 + 
            (self.z)**2 )**0.5
    


v1 = Vector3(4,3,5)

d1 = v1.len()
print(d1)




#Aufgabe 2
#Erstellen Sie eine Klasse WGS84Coord welche folgende Attribute hat:
#_longitude (=Länge)
#_latitude (=Breite)
#latitude hat den Wertebereich [-90,90] und longitude hat den Bereich [-180,180].
#Anforderungen:
#a) Im Konstruktor der Klasse kann die Länge und Breite übergeben werden. Der Standard-Wert ist 0.
#b) Stellen sie sicher, dass _longitude und _latitude immer im korrekten Wertebereich sind. Verwenden Sie dazu Setter- und Getter-Methoden Falls ein Wert ausserhalb des zulässigen Bereichs gesetzt wird, so wird dieser korrigiert und eine Warnung wird ausgegeben.
#c) Verwenden Sie Property Attribute anstatt Setter- und Getter-Methoden

class WGS84Coord:
    def __init__ (self, longitude = 0, latitude = 0):
        self.setLongitude(longitude)
        self.setLatitude(latitude)

    def setLongitude(self, value):
         if value < -180:
            raise ValueError("Die Longitude darf nicht kleiner als -180 sein.")
         if value > 180:
            raise ValueError("Die Longitude darf nicht grösser als 180 sein.")
         self._laenge = value
    
    def getLongitude(self):
        return self._laenge 
    
    def setLatitude(self, value):
         if value < -90:
            raise ValueError("Die Latitude darf nicht kleiner als -90 sein.")
         if value > 90:
            raise ValueError("Die Latitude darf nicht grösser als 90 sein.")
         self._breite = value

    def getLatitude(self):
        return self._breite
    
    
    
    
    
    
    Longitude = property(getLongitude, setLongitude)
    Latitude = property (getLatitude, setLatitude)

c1 = WGS84Coord(44, 22)

print(c1.Latitude, c1.Longitude)

#Musterlösung Aufgabe 2
class WGS84Coord:
    def __init__ (self, lng = 0, lat = 0):
        self.setLongitude(lng)
        self.setLatitude(lat)

    def setLongitude(self, lng):
        self._lng = lng

    def setLatitude(self, lat):  
         if lat > 90:
            self._lat = lat - 180 * (1+((lat - 90)//180))
         elif lat < -90:
             self.lat = lat + 180 * (1+((lat+90)//-180))
         else:
             self._lat = lat

    def getLongitude(self):
        return self._lng
    
    def getLatitude(self):
        return self._lat

pos1 = WGS84Coord(8.5, 47.3)

print(pos1.getLongitude(), pos1.getLatitude())