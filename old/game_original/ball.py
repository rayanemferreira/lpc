from config import *
from collision import  detection_collision
import math


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
        self.redox = [0.0, 0.0]
        self.rect = None

    def detection_collision(self, bullet):
        if bullet.rect.colliderect((self.x, self.y, 50, 50)):
            pos = -bullet.yp + self.y + 25
            pos *= 3.6
            pos_yp = -bullet.xp + self.x + 25
            pos_yp *= 3.6
            if (self.y < bullet.yp < self.y + 10 or self.y + 40 < bullet.yp < self.y + 50) and\
                    (self.x < bullet.xp < self.x + 10 or self.x + 40 < bullet.xp < self.x + 50):
                self.dx = 1 * math.sin(math.radians(pos_yp))
                self.dy = 1 * math.sin(math.radians(pos))

            elif self.y + 10 < bullet.yp < self.y + 40:
                self.dy = 1 * math.sin(math.radians(pos))
                if bullet.dx > 0:
                    self.dx = 1
                else:
                    self.dx = -1

            elif self.x + 10 < bullet.xp < self.x + 40:
                self.dx = 1 * math.sin(math.radians(pos_yp))
                if bullet.dy > 0:
                    self.dy = 1
                else:
                    self.dy = -1
            self.redox[0] = self.dx / 10
            self.redox[1] = self.dy / 10
            return True
        return False

    def move(self):
        self.rect = pygame.Rect(self.x, self.y, 50, 50)
        if not detection_collision(self.rect):
            self.dy *= -1
            self.y = self.y + self.dy
            rect = pygame.Rect(self.x, self.y, 50, 50)
            if not detection_collision(rect):
                self.dx *= -1
                self.dy *= -1
                self.x = self.x + self.dx
                print(self.dx, self.dy)
            self.per = False
        else:
            self.per = True

        self.x += self.dx
        self.y += self.dy
        self.draw()
        self.speed(self.per)

    def draw(self):
        screen.blit(self.surface, (self.x, self.y))

    def speed(self, per):
        if not per:
            if math.fabs(self.dx) > 0.1 or math.fabs(self.dy) > 0.1:
                if self.dx > 0:
                    self.dx -= self.redox[0]
                if self.dx < 0:
                    self.dx += self.redox[0]
                if self.dy > 0:
                    self.dy -= self.redox[1]
                if self.dy < 0:
                    self.dy += self.redox[1]
            else:
                self.dx = self.dy = 0
                return

    def get_rect(self):
        return pygame.Rect(self.x, self.y, 50, 50)

    def restart(self):
        self.x, self.y = self.original[0], self.original[1]
        self.dx = self.dy = 0
