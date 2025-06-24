import pygame
from sys import exit
pygame.init()
# Initialize pygame and set up the display
pygame.display.set_caption("Dodging Game")
width = 800
height = 600
fps = 60
screen = pygame.display.set_mode((width, height))
# Set up the clock for controlling the frame rate
clock = pygame.time.Clock()
# Create a test surface to display
width_ts = 200
height_ts = 200
test_surface = pygame.Surface((width_ts, height_ts))
test_surface.fill((255, 0, 0))  # Fill the surface with red color
# Main game loop
game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.fill((0, 0, 0))
    screen.blit(test_surface, (0, 0))
    pygame.display.update()
    clock.tick(fps)