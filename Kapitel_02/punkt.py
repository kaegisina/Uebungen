class Punkt:
     def __init__(self, x=0, y=0):
         self.x = x
         self.y = y
     
     def __str__ (self):
          return f"[{self.x},{self.y}]"
     
     def __eq__(self, other):
          return self.x == other.x and self.y == other.y
     
     

p1 = Punkt(3,4)
p2 = Punkt (10,20)

print(p1)
print(p2)