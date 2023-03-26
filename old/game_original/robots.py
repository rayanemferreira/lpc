
from config import *


class Robots:
    def __init__(self, yp, xp, w, h, edge, color):
        self.xp = xp
        self.yp = yp
        self.dy = 0.05
        self.w = w
        self.h = h
        self.screen = edge
        self.color = color

    def detection(self):
        if self.yp > 670:
            self.dy *= -1
        elif self.yp < 75:
            self.dy *= -1

    def move(self):
        self.detection()
        self.yp += self.dy
        self.draw()

    def draw(self):
        pygame.draw.rect(self.screen, self.color, (self.xp, self.yp, self.w, self.h))

    def get_rect(self):
        return pygame.Rect(self.xp, self.yp, self.w, self.h)
