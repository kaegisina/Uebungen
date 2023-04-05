class Temperatur:
    def __init__(self, c = 0):
        self.c = c
    
    def __str__(self):
        return f"{self.c} °C"
    
    def __gt__(self, other):   #gt = greater than
        return self.c > other.c
    
    def __lt__(self, other):  #lt = less than
        return self.c < other.c
    
    def __eq__(self,other):   #eq = equal
        return self.c == other.c



t0 = Temperatur(10)
t1 = Temperatur(10)

if t1.c > t0.c:
    print("Nächste Woche ist die Temperatur höher")
elif t1.c < t0.c:
    print("Nächste Woche ist die Temperatur tiefer")
else:
    print("Nächste Woche ist die Temperatur gleich")