# Cody, 2021 August 28
# Collision detection is faster when you have quadtrees!
# With Daniel Shiffman
#
# v0.01  - Create the Particle class
# v0.02  - Make the particles check if they intersect, move, and highlight
# v0.021 - Make intersection line
# v0.03  - Use quadtrees to detect collisions


class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.r = 12
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
        
        
def setup():
    global particles
    colorMode(HSB, 360, 100, 100, 100)
    size(600, 400)
    particles = []
    for i in range(100):
        particles.append(Particle(random(20, width-20), random(20, height-20)))
    
def draw():
    global particles
    background(210, 80, 32)
    
    for particle in particles:
        particle.reset_highlight()
    
    # Render the particles and check if particles are colliding with others.
    for particle in particles:
        for other in particles:
            if (particle != other) and (particle.intersects(other)):
                particle.highlight()
                

                
                
        
        particle.render()
        particle.move()
    
    
