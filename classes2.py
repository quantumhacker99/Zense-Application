#Importing required files
import pygame, math

#Initializing variables
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700

# Important values 
t = 0
dt = 0.0005

class Projectile:                                                                                       # Creating a class for our projectile
    def __init__(self,velocity, theta,t, SCREEN):                                                     # Passing parameters
        self.vel =  [velocity*math.cos(theta), velocity * math.sin(theta)]                              # Storing x and y velocities in a list
        self.theta = theta
        self.SCREEN = SCREEN
        self.t = t
                                                                     
        self. x = 0
        self.SIDE= 5
        self.y =  SCREEN_HEIGHT - self.SIDE
        self. l = [(0,0)]

    def move(self,g):
        self.x += self.vel[0] * dt                                                       # We increment x or y by dx or dy respectively every time move() is called. Then we use the principle that dx = v* dt
        self.y -= self.vel[1] * dt 

        self.vel[1] -= g*dt                                                                                 # Now, v also decreases by dv, which is g*dt.
    
        if  SCREEN_HEIGHT - self. y  < self.SIDE or self. y <= 0 :                                           # Conditions for collisions with floor, walls, or ceiling. Here coefficient of restitution is 1, and the collision is thus elastic and loses no kinetic energy.
            self.vel[1] *= -1
        if SCREEN_WIDTH - self.x < self.SIDE or self.x  <=  0:
            self.vel[0] *= -1
    
    def draw(self):
        return pygame.draw.rect(self.SCREEN, (255,255,255), (self.x, self.y, self.SIDE, self.SIDE))         # A draw function which draws our projectile
    
    def pixel(self):
        if (int(self.x)+self.SIDE/2, int(self.y)+ self.SIDE/2) == self.l[ - 1]:                             # Creating the red and blue tail which follows around, tracing the path.

            pass

        else:
            
            self.l.append((int(self.x)+self.SIDE/2, int(self.y)+ self.SIDE/2))
        
        if len(self.l) >= 100:
            self.l.pop(0)
        return self.l

