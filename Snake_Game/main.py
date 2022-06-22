# Modules used
import pygame, random, sys
from pygame.math import Vector2

# Initializes the game
pygame.init()

# Font
game_font = pygame.font.Font(none, 25)

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
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(1,0)
        self.new_block = False

    def draw_snake(self):
        for block in self.body:
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)# Create a rectangle
            pygame.draw.rect(display, (183, 111, 122), block_rect)# Draw a rectangle

    def move_snake(self):
        if self.new_block == True:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]

    def add_block(self):
        self.new_block = True
        
       
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
        self.check_fail()

    def draw_elements(self):
        self.prey.draw_prey()
        self.snake.draw_snake()

    def check_collision(self):#add another block to the snake
        if self.prey.pos == self.snake.body[0]:# Reposition the fruit
            self.prey.randomize()
            self.snake.add_block()

    def check_fail(self):
        # Checks if snake is outside of the screen
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            self.game_over()
        
        # Checks if snake hits itself
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    def game_over(self):
        pygame.quit()
        sys.exit()
    
    def draw_score(self):
        score_text = str(len(self.snaked.body) - 3)
        score_surface = game_font.render(score_text, True, (56, 74, 12))
        score.blit(score_surface, position)

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
                if main_game.snake.direction != 1:
                    main_game.snake.direction = Vector2(0, -1)
            if event.key == pygame.K_DOWN:
                if main_game.snake.direction != -1:
                    main_game.snake.direction = Vector2(0, 1)
            if event.key == pygame.K_LEFT:
                if main_game.snake.direction != 1:
                    main_game.snake.direction = Vector2(-1, 0)
            if event.key == pygame.K_RIGHT:
                if main_game.snake.direction != -1:
                    main_game.snake.direction = Vector2(1, 0)

    display.fill((80, 80, 80))
    main_game.draw_elements()
    pygame.display.update() # Refreshes the display
    clock.tick(60) # Sets the fps for the game
