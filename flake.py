# flake

import random
import pygame

pygame.init()

listOfPoint = [(450.0, 250.0), (350.0, 423.2050807568877), (150.00000000000006, 423.20508075688775), (50.0, 250.00000000000003), (149.99999999999991, 76.7949192431123), (350.0, 76.79491924311228)]

screen = pygame.display.set_mode((500, 500))
screen.fill((250, 250, 250))
pygame.draw.polygon(screen, (0, 0, 0), listOfPoint, 1)

newPointX = 200
newPointY = 200

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
    corner = random.randrange(6)

    vectX = listOfPoint[corner][0] - newPointX
    vectY = listOfPoint[corner][1] - newPointY

    newPointX = newPointX + vectX*2/3
    newPointY = newPointY + vectY*2/3

    pygame.draw.circle(screen, (255, 0, 0), (newPointX, newPointY), 1)

    pygame.display.flip()