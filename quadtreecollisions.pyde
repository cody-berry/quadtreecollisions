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
    global particles
    colorMode(HSB, 360, 100, 100, 100)
    size(600, 400)
    particles = []
    points = []
    for i in range(1000):
        particle = Particle(random(20, width-20), random(20, height-20))
        particles.append(particle)
        p = Point(particle.x, particle.y, particle)
        points.append(p)
        
    
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
                
                # Our goal for the code below is to create the average line
                # of intersection.
                # We need to figure out the distance PVector to compute the 
                # average point.
                distance = PVector(other.x, other.y).sub(PVector(particle.x, 
                                                                 particle.y))
                # We'll use direction and magnitude to compute the average
                # point.
                direction = distance.heading()
                magnitude = distance.mag()
                # Average is the average point, but in order to do that,
                # we need to add half the cosine of the angle times 
                # the magnitude of the distance divided by 2 and the
                # sine of the angle times the magnitude of the distance
                # divided by 2 to get the average point.
                average = PVector(particle.x + magnitude*cos(direction)/2, 
                                  particle.y + magnitude*sin(direction)/2)
                
                # We now want to show a line at the average point 
                # that is perpendicuular to our distance vector.
                pushMatrix()
                translate(average.x, average.y)
                # We're rotating to the direction that we want to be in,
                # the direction vector.
                rotate(direction)
                stroke(0, 50, 100)
                strokeWeight(1)
                # We want to draw a line perpendicular, not parellel!
                line(0, -15, 0, 15)
                popMatrix()
                noStroke()                
                
                
        
        particle.render()
        particle.move()
    
    print(frameRate)
    
    
