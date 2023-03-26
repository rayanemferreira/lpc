from config import *
import math
import time
from collision import detection_collision


class Ball:
    def __init__(self, xp, yp, w, h):
        self.x = xp
        self.y = yp
        self.image = pygame.image.load("sprites/ball.png")
        self.surface = pygame.transform.scale(self.image, (w, h))
        self.dx = 0
        self.original = (xp, yp)
        self.dy = 0
        self.per = False

    def detection_collision(self, bullet):
        if bullet.rect.colliderect((self.x, self.y, 50, 50)):
            pos = bullet.rect.x - self.x
            if pos > 25:
                self.dx = -1
                self.dy = -1
                self.move()
            elif pos == 25:
                self.dx = 1
                self.dy = 0
                self.move()
            else:
                self.dx = 1
                self.dy = -1
                self.move()
            return True
        return False

    def move(self):

        if self.x <= 25 or self.x >= 1200:
            self.dx *= -1
            self.per = False

        elif self.y <= 75 or self.y >= 700:
            self.dy *= -1
            self.per = False
        else:
            self.per = True
            if not detection_collision(self.get_rect()):
                print("colidiu")
                self.dy *= -1

        self.x += self.dx
        self.y += self.dy
        self.draw()
        self.speed(self.per)

    def draw(self):
        screen.blit(self.surface, (self.x, self.y))

    def speed(self, per):
        if not per:
            if math.fabs(self.dx) > 0.1 and math.fabs(self.dy) > 0.1:
                if self.dx > 0:
                    self.dx -= 0.1
                if self.dx < 0:
                    self.dx += 0.1
                if self.dy > 0:
                    self.dy -= 0.1
                if self.dy < 0:
                    self.dy += 0.1
            else:
                self.dx = self.dy = 0
                return

    def get_rect(self):
        return pygame.Rect(self.x, self.y, 50, 50)

    def restart(self):
        self.x, self.y = self.original[0], self.original[1]
        self.dx = self.dy = 0
