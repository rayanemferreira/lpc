from blocks import Blocks
from config import*
import pygame


class Arena:
    def __init__(self, map_name, screen):
        self.map_name = map_name
        self.screen = screen

    def draw_object(self):
        blocks = Blocks(self.map_name)
        list_rect = []
        for i in blocks.blocks():
            aux = pygame.draw.rect(self.screen, "#C89632", (i[1] * 20, i[0] * 20, 20, 20))
            list_rect.append(aux)

        return list_rect
