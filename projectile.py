#importing required file
import pygame, math,closepygame 
from classes2 import *                              

#Initialization
SCREEN_WIDTH = 700                                  
SCREEN_HEIGHT = 700



planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

pygame.init()

run = True

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))                     #Initializing variables
keys = pygame.key.get_pressed()

g_list = [3.59, 8.87, 9.81, 3.77, 25.95, 11.08, 10.67, 14.07, 0.42]
a = 0

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Projectile Motion")
screen.blit(SCREEN,(-500,0))
velocity = 100
theta = 45

projectile = Projectile( velocity, theta,t, SCREEN)                         # creating object
gravity = g_list[0] 


#SCREEN.blit(mercury, (0,0))
def printing_statement(a):
    print "The current planet is "+planets[a]+" with a gravity of "+str(gravity) + " m/s^2"


while run:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:                                    # Taking key input to change the gravity and thereby 
            if event.key ==  pygame.K_1:
                a = 0
                printing_statement(a)
                
            elif event.key == pygame.K_2:
                a = 1
                gravity = g_list[a]
                printing_statement(a)      
            elif event.key == pygame.K_3:
                a = 2 
                gravity = g_list[a]
                printing_statement(a)       
               
            elif event.key == pygame.K_4:
                a = 3
                gravity = g_list[a]
                printing_statement(a)       
              
            elif event.key == pygame.K_5:
                a = 4
                gravity = g_list[a]
                printing_statement(a)       

            elif event.key == pygame.K_6:
                a = 5
                gravity = g_list[a]
                printing_statement(a)       
            
            elif event.key ==  pygame.K_7:
                a = 6
                gravity = g_list[a]
                printing_statement(a)       
           
            elif event.key == pygame.K_8:
                a = 7
                gravity = g_list[a]
                printing_statement(a)       
          
    projectile.draw()
    projectile.move(gravity)                                                          # Drawing and moving the box
    l = projectile.pixel()
    for i in l[0:20]:
        SCREEN.set_at((int(i[0]),int(i[1])), (0,0,255))                 # Adding different colours to create a tail
    for i in l[20:200]:
        SCREEN.set_at((int(i[0]),int(i[1])), (255, 0, 0))
    for i in l[200:500]:
        SCREEN.set_at((int(i[0]),int(i[1])), (0,255,255))

    t += dt                                                             # Incrementing the time
    pygame.display.flip()
    closepygame.close()                                                 # Instructions to close file, by recording event of pressing X button 
    
