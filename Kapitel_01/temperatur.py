class Temperatur():
    def __init__ (self,c):
        self._celsius = c
        self.setTemperatur(c)

    def getKelvin(self):
        return self._celsius+273.15
    
    def setKelvin(self, value):
        self._celsius = value - 273.15
    
    def setTemperatur(self,value):
        if value < -273.15:
            raise ValueError("Die Temperatur darf nicht kleiner als -273.15C sein.")
        self._celsius = value

    def getTemperatur(self):
        return self._celsius
    
    celsius = property(getTemperatur, setTemperatur)
    kelvin = property(getKelvin, setKelvin)
    


basel = Temperatur(7)
print(basel.kelvin())
#so Temperatur überschreiben
basel.setTemperatur(17)
print(basel.kelvin())

#Funktionen mit _ darf man von aussen nicht aufrufen! daher so nicht erlaubt:
basel = Temperatur(7)
print(basel._celsius, "°C")

#daher so machen mit getTempertatur:
v = basel.getTemperatur()
print(v, "°C")

basel = Temperatur(7)
#setTemperatur wird aufgerufen:
basel.celsius = 30
print(basel.kelvin())
print(basel.celsius)

basel = Temperatur(7)
basel.kelvin = 280.15
print(basel.kelvin)


test = Temperatur(-500)
print(test.kelvin())

test2 = Temperatur(0)
test2._celsius = -500

print(test.kelvin())


