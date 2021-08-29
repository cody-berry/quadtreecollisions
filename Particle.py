


class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.r = 4
        self.highlighted = False
        
    
    def render(self):
        noStroke()
        if self.highlighted:
            fill(0, 0, 100)
        else:
            fill(0, 0, 50)
        circle(self.x, self.y, self.r*2)
    
    
    def move(self):
        self.x += random(-1, 1)
        self.y += random(-1, 1)
    
    
    def intersects(self, other):
        return dist(self.x, self.y, other.x, other.y) < self.r + other.r
    
    
    def highlight(self):
        self.highlighted = True
        
    
    def reset_highlight(self):
        self.highlighted = False
