


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
        self.highlighted = False
    
    
    def move(self):
        self.x += random(-1, 1)
        self.y += random(-1, 1)
    
    
    def intersects(self, other):
        return dist(self.x, self.y, other.x, other.y) < self.r + other.r
    
    
    def highlight(self):
        self.highlighted = True
        
    
    def reset_highlight(self):
        self.highlighted = False
        
        
    # Edge check is very important for quadtrees. Otherwise the quadtree
    # won't detect collisions there!
    def edge_check(self):
        # edges that are pointed vertically below
        if self.x + self.r > width: # right
            self.x = self.r
            
        if self.x - self.r < 0: # left
            self.x = width - self.r
            
        # edges that are pointed horizontally below
        if self.y - self.r < 0: # top
            self.y = height - self.r
            
        if self.y + self.r > height: # bottom
            self.y = self.r
