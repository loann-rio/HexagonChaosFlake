import random
import pygame

pygame.init()

# vertex of the hexagone
listOfPoint = [(450.0, 250.0), (350.0, 423.20), (150, 423.20), (50.0, 250), (150, 76.79), (350.0, 76.79)]

# init screen
screen = pygame.display.set_mode((500, 500))
screen.fill((250, 250, 250))
pygame.draw.polygon(screen, (0, 0, 0), listOfPoint, 1)

newPointX = 200
newPointY = 200

for i in range(60000):

    # chose a random vertex
    corner = random.randrange(6)

    # get vector btw current point and vertex
    vectX = listOfPoint[corner][0] - newPointX
    vectY = listOfPoint[corner][1] - newPointY

    # get new point
    newPointX = newPointX + vectX*2/3
    newPointY = newPointY + vectY*2/3

    # draw new point
    pygame.draw.circle(screen, (255, 0, 0), (newPointX, newPointY), 1)

    # draw
    pygame.display.flip()