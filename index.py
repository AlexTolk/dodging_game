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
text_font_collide = pygame.font.Font('assets/prstartk.ttf', 50)
text_collide = text_font_collide.render('OUCH!!!', False, 'Red')
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

hero_rect = hero.get_rect(center=(hero_x_pos, hero_y_pos))
pot_rect = pot.get_rect(center=(pot_x_pos, pot_y_pos))
candle_rect = candle.get_rect(center=(candle_x_pos, candle_y_pos))
box_rect = box.get_rect(center=(box_x_pos, box_y_pos))

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
    screen.blit(hero, hero_rect)
    screen.blit(candle, candle_rect)
    screen.blit(box, box_rect)
    screen.blit(pot, pot_rect)
    # Add movement
    candle_rect.left -= 4
    if candle_rect.left <= 400:
        pot_flag = True
    if pot_flag:
        pot_rect.left -= 4
    if pot_rect.left <= 400:
        box_flag = True
    if box_flag:
        box_rect.left -= 4
    # Return objects to their initial position
    if candle_rect.right <= 0:
        candle_rect.left = 800
    if pot_rect.right <= 0:
        pot_rect.left = 800
    if box_rect.right <= 0:
        box_rect.left = 1000
    # collect inputs
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        hero_rect.top -= 20
    if keys[pygame.K_DOWN]:
        hero_rect.top += 20
    # output collision message
    if hero_rect.colliderect(candle_rect) or hero_rect.colliderect(pot_rect) or hero_rect.colliderect(box_rect):
        screen.blit(text_collide, (200, 165))
    pygame.display.update()
    clock.tick(fps)