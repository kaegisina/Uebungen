import shapely
from shapely.geometry import Point, Polygon, MultiPolygon, MultiPoint
from shapely import wkt
import matplotlib.pyplot as plt

Muttenz = Point([ 7.6424084, 47.5347037])
print(Muttenz.wkt)

s = "POINT (7.6424084 47.5347037 )"

p = wkt.loads(s)

file = open("Kapitel_09/schweiz.wkt")
ch = file.read()
file.close()


schweiz = wkt.loads(ch)

if Muttenz.within(schweiz):
    print("Ja, Muttenz ist innerhalb der Schweiz")
else:
    print("Nein, Muttenz gehört leider nicht zur Schweiz")

for geometry in schweiz.geoms:
    x,y = geometry.exterior.xy
    plt.plot(x,y)

plt.show()