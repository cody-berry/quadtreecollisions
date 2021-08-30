# Cody, 2021 August 28
# Collision detection is faster when you have quadtrees!
# With Daniel Shiffman
#
# v0.01  - Create the Particle class
# v0.02  - Make the particles check if they intersect, move, and highlight
# v0.021 - Add intersection line
# v0.03  - Use quadtrees to detect collisions


from Particle import *
from Point import *
from Quadtree import *
from Rectangle import *
        
        
def setup():
    global particles, points, qt
    colorMode(HSB, 360, 100, 100, 100)
    size(600, 400)
    particles = []
    points = []
    # boundary = Rectangle(0, 0, width, height)
    # qt = Quadtree(boundary, 4)
    for i in range(1000):
        particle = Particle(random(width), random(height-20))
        particles.append(particle)
        # p = Point(particle.x, particle.y, particle)
        # points.append(p)
        # qt.insert(p)
        
    
def draw():
    global particles, points, qt
    background(210, 80, 32)
    boundary = Rectangle(0, 0, width, height)
    qt = Quadtree(boundary, 4)
    
    for particle in particles:
        p = Point(particle.x, particle.y, particle)
        # particle.reset_highlight()
        qt.insert(p)
    
    # Render the particles and check if particles are colliding with others.
    for particle in particles:
        side = 30
        others = qt.query(Rectangle(particle.x - side/2, particle.y - side/2, 
                                    side, side))
        # others = qt.query(Rectangle(particle.x-15, particle.y-15, 30, 30))
        # stroke(210, 100, 50)
        # noFill()
        # rect(p.data.x - side/2, p.data.y - side/2, side, side)
        
        for other in others:
            if (particle != other.data) and (particle.intersects(other.data)):
                particle.highlight()
                
                # # Our goal for the code below is to create the average line
                # # of intersection.
                # # We need to figure out the distance PVector to compute the 
                # # average point.
                # distance = PVector(other.data.x, other.data.y).sub(PVector(
                #                                                            p.data.x, 
                #                                                           p.data.y))
                # # We'll use direction and magnitude to compute the average
                # # point.
                # direction = distance.heading()
                # magnitude = distance.mag()
                # # Average is the average point, but in order to do that,
                # # we need to add half the cosine of the angle times 
                # # the magnitude of the distance divided by 2 and the
                # # sine of the angle times the magnitude of the distance
                # # divided by 2 to get the average point.
                # average = PVector(p.data.x + magnitude*cos(direction)/2, 
                #                   p.data.y + magnitude*sin(direction)/2)
                
                # # We now want to show a line at the average point 
                # # that is perpendicuular to our distance vector.
                # pushMatrix()
                # translate(average.x, average.y)
                # # We're rotating to the direction that we want to be in,
                # # the direction vector.
                # rotate(direction)
                # stroke(0, 50, 100)
                # strokeWeight(1)
                # # We want to draw a line perpendicular, not parellel!
                # line(0, -15, 0, 15)
                # popMatrix()
                # noStroke()                
                
                
    for particle in particles:  
        particle.move()  
        particle.render()
        # particle.edge_check()
        
    qt.show()
    
    print(frameRate)
    
    
