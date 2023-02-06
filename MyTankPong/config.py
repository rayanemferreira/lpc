import pygame
from arena import Arena

sc_width = 1280
sc_height = 720

# COLORS (RGB)
RED = (200, 0, 0)
GREEN = (8, 252, 4)
BLUE = (50, 75, 200)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

TURN_SPEED = 5
MOVE_SPEED = 5
BULLET_SPEED = 10

MAP_NAME = "classic"
touch_limit = 3
bullet_limit = 3
border = 0

screen = pygame.display.set_mode((sc_width, sc_height))
arena = Arena(MAP_NAME, screen)
