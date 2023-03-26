import random
import pygame
from constants.const import *
from constants.colors import *

def displaySomeText(text, y_coord, font, surf):
    somewords = font.render(
        text,
        True,
        random.choice(title_colors))
    width, _ = pygame.font.Font.size(font, text)
    position_font = (SCREENSIZE[0] - width) / 2
    surf.screen.blit(somewords, (position_font + 6, y_coord))
    surf.screen.blit(somewords, (position_font + 6, y_coord))