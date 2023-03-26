import pygame
from constants.colors import BULLETS, BLACK
from random import choice
from constants.const import PROJ_VELOCITY, DPROJ_VELOCITY, SCREENSIZE, BORDER_W
from playsound import playsound
class Bullet(pygame.sprite.Sprite):
    """
    A classs for the bullets
    """
    def __init__(self, x, y, dir):
        playsound('./audio/shoot.mp3', block=False)
        pygame.sprite.Sprite.__init__(self)
        self.color = choice(BULLETS)
        self.dir = dir
        self.movx = 0
        self.movy = 0



        v = PROJ_VELOCITY if len(dir)<1 else DPROJ_VELOCITY

        if 'N' in dir:
            self.movy = -v
        elif 'S' in dir:
            self.movy = v

        if 'W' in dir:
            self.movx = -v
        elif 'E' in dir:
            self.movx = v

        kill = 0
        if len(dir)==1 and (dir=='N' or dir=='S'):
            rotation = 90
        elif len(dir)==1 and (dir=='E' or dir=='W'):
            rotation = 0
        elif 'NE'==dir or 'SW'==dir or 'EN'==dir or 'WS'==dir:
            rotation = 45
        elif 'NW'==dir or 'WN'==dir or 'SE'==dir or 'ES'==dir:
            rotation = 315
        else:
            kill = 1
            rotation = 0

        self.image = pygame.Surface([25, 8])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        pygame.draw.rect(self.image, self.color, pygame.Rect(0, 0, 25, 5), border_radius=3)
        self.image = pygame.transform.rotate(self.image, rotation)

        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

        if kill:
            self.kill()
            del self



    def update(self, _, __):
        self.rect.center = self.rect.center[0] + self.movx, self.rect.center[1] + self.movy
        if (not (SCREENSIZE[1]-BORDER_W-30 >= self.rect.y >= 30 + BORDER_W) ) or\
                (not (SCREENSIZE[0]-BORDER_W*4 -5 >= self.rect.x >= BORDER_W*2 - 5)):
            self.kill()
            del self
            return