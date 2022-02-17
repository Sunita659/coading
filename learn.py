
import pygame, sys

pygame.init()
clock=pygame.time.Clock()

screen = pygame.display.set_mode((400,600))

#creating objects of game
#pink
r1=pygame.Rect(100,300,30,30)
speedr1=-2

#blue
r2=pygame.Rect(300,300,30,30)
speedr2=2

#green
r3=pygame.Rect(200,200,30,30)
speedr3=-2

#white
r4=pygame.Rect(200,400,30,30)
speedr4=2

while True:    
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    #code for moving r1,r2,r3        
    r1.x=r1.x+speedr1
    r2.x=r2.x+speedr2
    
    r3.y=r3.y+speedr3
    r4.y=r4.y+speedr4#add code for moving the r4 box here
    
    
    #code for changing direction of r1,r2,r3 after reaching the edge
    if(r1.x <0):
        speedr1=speedr1 * -1
    if(r1.x >400):
        speedr1=speedr1 * -1

    if(r2.x <0):
        speedr2=speedr2 * -1
    if(r2.x >400):
        speedr2=speedr2 * -1

    if(r3.y <0):
        speedr3=speedr3 * -1
    if(r3.y >600):
        speedr3=speedr3 * -1

    if(r4.y <0):
        speedr4=speedr4* -1
    if(r4.y >600):#add if conditions to make r4 move back after reaching top or bottom edge
        speedr4=speedr4 * -1
    
        
   

    
    pygame.draw.rect(screen,(223,100,100),r1)
    pygame.draw.rect(screen,(23,100,200),r2)
    pygame.draw.rect(screen,(23,200,80),r3)
    pygame.draw.rect(screen,(200,200,200),r4)
    
    
    pygame.display.update()
    clock.tick(30)

