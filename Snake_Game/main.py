# Modules used
import pygame, random, sys
from pygame.math import Vector2

# Initializes the game
pygame.init()

# Cells
cell_size = 30
cell_number = 20

# Creates the game screen
display = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))

# Creates a surface/text
surface = pygame.Surface((100,200))
surface.fill(pygame.Color('blue'))

# Rectangle
rect = surface.get_rect(center = (400, 400))

# FPS
clock = pygame.time.Clock()

# Snake
class SNAKE:
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(6, 10), Vector2(7, 10)]
        self.direction = Vector2(1,0)

    def draw_snake(self):
        for block in self.body:
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)# Create a rectangle
            pygame.draw.rect(display, (183, 111, 122), block_rect)# Draw a rectangle

    def move_snake(self):
        body_copy = self.body[:-1]
        body_copy.insert(0, body_copy[0] + self.direction)
        self.body = body_copy[:]
       
# Prey
class PREY:
    def __init__(self):
        self.randomize()
    
    def draw_prey(self): # Draw a square
        prey_rect = pygame.Rect(int(self.pos.x * cell_size),int(self.pos.y * cell_size), cell_size, cell_size)
        pygame.draw.rect(display, (100,75,0), prey_rect)

    def randomize(self):
        self.x = random.randint(0,cell_number - 1)
        self.y = random.randint(0,cell_number - 1)
        self.pos = Vector2(self.x, self.y)
# Main
class MAIN():
    def __init__(self):
        self.snake = SNAKE()
        self.prey = PREY()

    def update(self):
        self.snake.move_snake()
        self.check_collision()

    def draw_elements(self):
        self.prey.draw_prey()
        self.snake.draw_snake()

    def check_collision(self):# Reposition the fruit, add another block to the snake
        if self.prey.pos == self.snake.body[0]:
            self.prey.randomize()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,150)

main_game = MAIN()

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() 
            sys.exit()# Quits the game
        if event.type == SCREEN_UPDATE:
            main_game.update()
        # Keystrokes
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                main_game.snake.direction = Vector2(0, -1)
            if event.key == pygame.K_DOWN:
                main_game.snake.direction = Vector2(0, 1)
            if event.key == pygame.K_LEFT:
                main_game.snake.direction = Vector2(-1, 0)
            if event.key == pygame.K_RIGHT:
                main_game.snake.direction = Vector2(1, 0)

    display.fill((80, 80, 80))
    main_game.draw_elements()
    pygame.display.update() # Refreshes the display
    clock.tick(60) # Sets the fps for the game
