import pygame, random

# Initializes the game
pygame.init()

# Creates the game screen
display = pygame.display.set_mode((800, 800))

# FPS
clock = pygame.time .Clock()

# Initial game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()