punktnummer = 1
x = 2600000
y = 1200000
h = 540.15

print(punktnummer, x, y, h)

# so sollte man es nicht machen:
punkt1 = [1,260000, 1200000, 540.15]
punkt2 = [2, 0, 0, 0]


from punkt import*


p1 = Punkt(1, 2600000, 1200000, 540.15)
p2 = Punkt(2, 0, 0, 0)

def hdiff(punkt1, punkt2):
    return abs(punkt1.h-punkt2.h)

d1 = p1.dist(p2)
d2 = p2.dist(p1)
print(d1,d2)

dh = p1.hdiff(p2)
print(dh)

dh= abs(p1.h-p2.h)
print(dh)

print(p1.x, p1.y, p1.h)
print(p2.x, p2.y, p2.h)

p1.anzeigen()
p2.anzeigen()

#man kann x überschreiben:
p1.x = 50
p1.anzeigen ()