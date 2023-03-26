import pygame
from constants.const import *
from constants.colors import *


class Border(pygame.sprite.Sprite):
    """
    This border class is drawn around the edge of the screen. it is a sprite itself, so it cannot be killed
    """

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.color = (255,0,0)
        self.image = pygame.Surface((SCREENSIZE[0], SCREENSIZE[1]))
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        self.drawrect()
        self.rect.center = (SCREENSIZE[0]/2, SCREENSIZE[1]/2)

    def update(self,_,__):

        r,g,b = self.color
        if r>0 and b == 0:
            r -= BORDERSPEED
            g += BORDERSPEED
        if g > 0 and r == 0:
            g -= BORDERSPEED
            b += BORDERSPEED
        if b > 0 and g == 0:
            b -= BORDERSPEED
            r += BORDERSPEED
        self.color = (r,g,b)
        self.drawrect()

    def drawrect(self):
        self.lines = [
            pygame.draw.line(self.image, self.color, [0, 30], [SCREENSIZE[0], 30], BORDER_W),
            pygame.draw.line(self.image, self.color, [0, SCREENSIZE[1]], [SCREENSIZE[0], SCREENSIZE[1]], BORDER_W*2),
            pygame.draw.line(self.image, self.color, [0, 30], [0, SCREENSIZE[1]], BORDER_W*2),
            pygame.draw.line(self.image, self.color, [SCREENSIZE[0], 30], [SCREENSIZE[0], SCREENSIZE[1]], BORDER_W*2)
]

        self.rect = self.image.get_rect()

    def die(self):
        return