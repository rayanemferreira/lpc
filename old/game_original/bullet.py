import math

from config import *
from collision import detection_collision


class Bullet:
    def __init__(self, xp, yp, angle, color_bullet):
        self.count = 0
        self.angle = angle
        self.rect = None
        self.xp = 25 + xp + 25 * math.cos(math.radians(self.angle))
        self.yp = 25 + yp - 25 * math.sin(math.radians(self.angle))
        self.dx = speed_ball * math.cos(math.radians(self.angle))
        self.dy = speed_ball * -math.sin(math.radians(self.angle))
        self.color = color_bullet

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.xp, self.yp, 5, 5))

    def move(self):
        self.rect = pygame.Rect(self.xp, self.yp, 5, 5)

        if not detection_collision(self.rect):
            self.dy *= -1
            self.yp = self.yp + self.dy * 2
            rect = pygame.Rect(self.xp, self.yp, 5, 5)
            self.count += 1
            if not detection_collision(rect) and not (self.xp == -50):
                self.dx *= -1
                self.dy *= -1
                self.xp = self.xp + self.dx * 2

        self.xp = self.xp + self.dx
        self.yp = self.yp + self.dy
        self.draw()

        if self.count > touch_limit:
            self.xp = -50

    def get_data(self):
        rect = pygame.Rect(self.xp, self.yp, 5, 5)
        return rect, self.count, self.color
