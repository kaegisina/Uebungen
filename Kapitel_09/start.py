from pyproj import Transformer

lat = 47.5347037
lng = 7.6424084

t = Transformer.from_crs("EPSG:4326", "EPSG:2056")

r = t.transform(lat,lng)

print(r)

t2 = Transformer.from_crs("EPSG:2056", "EPSG:4326")

r2 = t2.transform(2615344.772462617, 1264905.7647697437)

print(r2)