import pygame
from pygame.locals import *
from pygame import mixer
pygame.init()

# Background colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
TEAL = (0, 80, 80)

# Display Background
size = (800, 768)
screen = pygame.display.set_mode(size)
bg_img = pygame.image.load('Assets/Images/blue_carbon_background.jpg')
bg_img = pygame.transform.scale(bg_img, (size))
pygame.display.set_caption("Furry Playhouse")


# Game will continue until user exits game
mainGameloop = True

#Controls how fast screen is up
clock = pygame.time.Clock()

# Program loop
while mainGameloop:
    screen.blit(bg_img,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainGameloop = False
    pygame.display.update()
pygame.quit()

# Initialize mixer in the program
mixer.init()
mixer.music.load('Assets/Music_Files/')
mixer.music.play()

# Clears the screen
screen.fill(TEAL)

# Updates the screen with what's been drawn
pygame.display.flip()
# FPS
clock.tick(60)