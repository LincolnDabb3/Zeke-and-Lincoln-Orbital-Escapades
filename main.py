import pygame
import os
import random
import math

os.chdir(os.path.dirname(os.path.abspath(__file__)))
pygame.init()

# Load your image in here
#image = pygame.image.load('')

width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Orbital Escapades')
clock = pygame.time.Clock()

background = pygame.image.load("stars.jpg")
pointer = pygame.image.load("pointer.png")
pointer = pygame.transform.scale(pointer, (30, 45))

play = pygame.image.load("Orbitial Escapades.png")

planet = pygame.image.load("planet.png")
planet = pygame.transform.scale(planet, (30, 40))

HiConPlanet = pygame.image.load("HighContrastPlanet.png")
HiConPlanet = pygame.transform.scale(HiConPlanet, (30, 40))

EvilPlanet = pygame.image.load("EvilPlanet.png")
EvilPlanet = pygame.transform.scale(EvilPlanet, (30, 40))

DarkPlanet = pygame.image.load("DarkPlanet.png")
DarkPlanet = pygame.transform.scale(DarkPlanet, (30, 40))

planets = [planet,HiConPlanet,EvilPlanet, DarkPlanet]


x_pos = [] # X positions (not expositions, that's for movies)
y_pos = [] # Y positions
sx = [] # Speed Xs
sy = [] # Speed Ys

pygame.mouse.set_visible(False)

# Load the music file
pygame.mixer.music.load("Danger.mp3")

# Play the music (loops=-1 means infinite loop)
pygame.mixer.music.play(-1)

# click (bite) SFX
click_sound = pygame.mixer.Sound("Bite.wav")


playing = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            click_sound.play()
            if playing:
                if event.button == 1: # 1 is Left Click
                    print(f"Left click at {event.pos}")
                    x_pos.append(event.pos[0])
                    y_pos.append(event.pos[1])
                    sx.append(random.random() * 100 - 50)
                    sy.append(random.random() * 100 - 50)
                elif event.button == 3: # 3 is Right Click
                    print("Right click!")
                    for i in range (100):
                        x_pos.append(random.random() * 800)
                        y_pos.append(random.random() * 600)
                        sx.append(random.random() * 100 - 50)
                        sy.append(random.random() * 100 - 50)
            else:
                playing = True
    
    if playing:

        screen.fill((255, 255, 255))
        screen.blit(background, (0, 0))
        screen.blit(pointer, (pygame.mouse.get_pos()[0] - 0, pygame.mouse.get_pos()[1] - 10))

        for i in range(sx.__len__()):
            screen.blit(planets[i % len(planets)], (x_pos[i], y_pos[i]))

            sx[i] += (pygame.mouse.get_pos()[0] - x_pos[i]) / 60
            sy[i] += (pygame.mouse.get_pos()[1] - y_pos[i]) / 60

            x_pos[i] += sx[i] / 2
            if (x_pos[i] > screen.get_width() - 20):
                sx[i] = -math.fabs(sx[i])
                x_pos[i] += sx[i] / 2

            if (x_pos[i] < 0):
                sx[i] = math.fabs(sx[i])
                x_pos[i] += sx[i] / 2

            y_pos[i] += sy[i] / 2
            if (y_pos[i] > screen.get_height() - 40):
                sy[i] = -math.fabs(sy[i])
                y_pos[i] += sy[i] / 2

            if (y_pos[i] < 0):
                sy[i] = math.fabs(sy[i])
                y_pos[i] += sy[i] / 2

            sx[i] *= 0.999
            sy[i] *= 0.999

        pygame.display.flip()
        clock.tick(60)

    else:

        screen.blit(play, (0, 0))
        screen.blit(pointer, (pygame.mouse.get_pos()[0] - 0, pygame.mouse.get_pos()[1] - 10))

        pygame.display.flip()
        clock.tick(60)

pygame.quit()
