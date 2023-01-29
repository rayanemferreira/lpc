import pygame


class Bullet(object):
    def __init__(self, point, cosine, sine):
        self.img = pygame.image.load("Sprites/obstacle.png")
        self.rect = self.img.get_rect()
        self.point = point
        self.x, self.y = self.point
        self.w = 4
        self.h = 4
        self.c = cosine
        self.s = sine
        self.xv = self.c * 10
        self.yv = self.s * 10

    def move(self):
        self.x += self.xv
        self.y -= self.yv

    def draw(self, screen):
        # screen.blit(self.img, [self.x, self.y, self.w, self.h])
        pygame.draw.rect(screen, (252, 180, 108),
                         [self.x, self.y, self.w, self.h])

    def get_rect(self):
        return self.rect
