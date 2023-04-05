class Punkt:
    def __init__(self, n, x, y, h):
        self.n = n
        self.x = x
        self.y = y
        self.h = h

    def anzeigen(self):
        print(self.n, self.x, self.y, self.h)

    def hdiff(self, other):
        return abs(self.h-other.h)
    
    def dist(self, other):
        return( (self.x-other.x)**2 + 
                (self.y-other.y)**2 + 
                (self.h - other.h)**2 )**0.5
    



