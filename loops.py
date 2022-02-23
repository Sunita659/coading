
import pygame, sys

pygame.init()
clock=pygame.time.Clock()

screen = pygame.display.set_mode((400,600))

#creating objects of game
tomatoes=[]
mushrooms=[]
carrots=[]
brinjals=[]
pumpkins=[]

for i in range(1,6):
    tomatoes.append(pygame.Rect(i*60,50,40,40))
for i in range(1,6):
    mushrooms.append(pygame.Rect(i*60,50,40,40))
for i in range(1,6):
    carrots.append(pygame.Rect(i*60,50,40,40))
for i in range(1,6):
    brinjals.append(pygame.Rect(i*60,50,40,40))
for i in range(1,6):
    pumpkins.append(pygame.Rect(i*60,50,40,40))
    
        
while True:    
    screen.fill((30,80,20))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
             
    for tomato in tomatoes:
        pygame.draw.Rect(screen,(223,50,50),tomato)
    for mushroom in mushrooms:
        pygame.draw.Rect(screen,(220,220,220),mushroom)
    for carrot in carrots:
        pygame.draw.Rect(screen,(250,20,20),carrot)
    for brinjal in brinjals:
        pygame.draw.Rect(screen,(150,50,220),brinjal)
    for pumpkin in pumpkins:
         pygame.draw.Rect(screen,(223,250,20),pumpkin)
    
    
    pygame.display.update()
    clock.tick(30)

