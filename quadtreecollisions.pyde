# Cody, 2021 August 28
# Collision detection is faster when you have quadtrees!
# With Daniel Shiffman
#
# v0.01 - Create the Particle class
# v0.02 - Make the particles check if they intersect, move, and highlight
# v0.03 - Use quadtrees to detect collisions


class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.r = 4
        
    
    def render(self):
        noStroke()
        fill(0, 0, 70)
        circle(self.x, self.y, self.r*2)
        
        
def setup():
    global particles
    colorMode(HSB, 360, 100, 100, 100)
    size(600, 400)
    particles = []
    for i in range(1000):
        particles.append(Particle(random(width), random(height)))
    
def draw():
    global particles
    background(210, 80, 32)
    for particle in particles:
        particle.render()
    
    
