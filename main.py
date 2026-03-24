import pygame
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
pygame.init()

# Load your image in here
#image = pygame.image.load('')

width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Orbital Escapades')
clock = pygame.time.Clock()




running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    

    screen.fill((255, 255, 255))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()