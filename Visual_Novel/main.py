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
size = (700, 500)
screen = pygame.display.set_mode(size)
bg_img = pygame.image.load()
bg_img = pygame.transform.scale(bg_image, (size))
pygame.display.set_caption("Furry Playhouse")


# Game will continue until user exits game
mainGameloop = True

#Controls how fast screen is up
clock = pygame.time.Clock()

# Program loop
while mainGameloop:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainGameloop = False

# Initialize mixer in the program
mixer.init()
mixer.music.load('Music File/bensound-summer_wav_music.wav')
mixer.music.play()

# Clears the screen
    screen.fill(TEAL)

# Updates the screen with what's been drawn
    pygame.display.flip()
# FPS
    clock.tick(60)

