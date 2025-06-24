import pygame
from sys import exit
pygame.init()
# Initialize pygame and set up the display
pygame.display.set_caption("Dodging Game")
width = 800
height = 400
fps = 60
screen = pygame.display.set_mode((width, height))
# Set up the clock for controlling the frame rate
clock = pygame.time.Clock()
#Load fonts
text_font = pygame.font.Font('assets/prstartk.ttf', 15)
text_surface = text_font.render('Dodging game', False, 'White')
# Load images
back = pygame.image.load('assets/code_game_back_floor.webp').convert()
hero = pygame.image.load('assets/detective.webp').convert_alpha()
candle = pygame.image.load('assets/candlestick.webp').convert_alpha()
pot = pygame.image.load('assets/teapot.webp').convert_alpha()
box = pygame.image.load('assets/wooden_box.webp').convert_alpha()
#Set initial coordinates
hero_x_pos = 15
hero_y_pos = 130
pot_x_pos = 800
pot_y_pos = 275
candle_x_pos = 800
candle_y_pos = 30
box_x_pos = 800
box_y_pos = 180

pot_flag = False
box_flag = False

# Main game loop
game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.fill((0, 0, 0))
    screen.blit(back, (0, 0))
    back.blit(text_surface, (320, 15))
    screen.blit(hero, (hero_x_pos, hero_y_pos))
    screen.blit(candle, (candle_x_pos, candle_y_pos))
    screen.blit(pot, (pot_x_pos, pot_y_pos))
    screen.blit(box, (box_x_pos, box_y_pos))
    # Add movement
    candle_x_pos -= 4
    if candle_x_pos == 400:
        pot_flag = True
    if pot_flag:
        pot_x_pos -= 4
    if pot_x_pos == 400:
        box_flag = True
    if box_flag:
        box_x_pos -= 4

    # Return objects to their initial position
    if candle_x_pos == -100:
        candle_x_pos = 800
    if pot_x_pos == -100:
        pot_x_pos = 800
    if box_x_pos == -100:
        box_x_pos = 1000
    pygame.display.update()
    clock.tick(fps)