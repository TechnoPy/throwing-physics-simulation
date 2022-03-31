import pygame
from sys import exit
import math

pygame.init()
pygame.display.set_caption('Window Title')
try:
    velocity = int(input("Enter the velocity : "))
    acceleration_due_to_gravity = (float(input("Enter the acceleration due to gravity : ")))/10000.00
    angle_of_throw = int(input("Enter the angle of throw : "))
except:
    print("Enter only numerical values")
    exit()

horizontal_velocity = (math.cos(math.radians(angle_of_throw)) * velocity)/100.00
vertical_velocity = (math.sin(math.radians(angle_of_throw)) * velocity)/100.00

player_x_coordinate = 315
player_y_coordinate = 175

framerate = 100
clock = pygame.time.Clock()
surface = pygame.Surface((320, 180))
screen = pygame.display.set_mode((960, 540))

print("horiz : ", horizontal_velocity)
print("vertic : ", vertical_velocity)

while True:
    surface.fill((0, 0, 0))

    player_x_coordinate -= horizontal_velocity 
    player_y_coordinate -= vertical_velocity 
    vertical_velocity -= acceleration_due_to_gravity 

    if(player_y_coordinate >= 175 or player_x_coordinate <= 0):
        vertical_velocity = 0
        horizontal_velocity = 0
    
    pygame.draw.rect(surface, (255, 0, 0), pygame.Rect(player_x_coordinate, player_y_coordinate, 5, 5))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    screen.blit(pygame.transform.scale(surface, (960, 540)), (0,0))
    pygame.display.update()
    clock.tick(100)

    
