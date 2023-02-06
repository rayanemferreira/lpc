import math
from config import *
from collision import detection_collision


class Bullet:
    def __init__(self, xp, yp, angle, color_bullet):
        self.count = 0
        self.angle = angle
        self.rect = pygame.Rect(20 + xp + 20 * math.cos(math.radians(self.angle)),
                                20 + yp - 20 * math.sin(math.radians(self.angle)), 5, 5)
        self.dx = BULLET_SPEED * math.cos(math.radians(self.angle))
        self.dy = BULLET_SPEED * -math.sin(math.radians(self.angle))
        self.color = color_bullet
        self.sound_collision = pygame.mixer.Sound("sound/collision.mp3")
        self.sound_collision.set_volume(0.3)

    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)

    def move(self):
        if not detection_collision(self.rect):
            pygame.mixer.Channel(3).play(self.sound_collision)
            self.dy *= -1
            self.rect.y = self.rect.y + self.dy * 2
            rect = pygame.Rect(self.rect.x, self.rect.y, 5, 5)
            self.count += 1
            if not detection_collision(rect) and not (self.rect.x == -40):
                self.dx *= -1
                self.dy *= -1

                self.rect.x = self.rect.x + self.dx * 2

        if self.count > touch_limit:
            self.rect = pygame.Rect(-40, 0, 5, 5)

        self.rect.x = self.rect.x + self.dx
        self.rect.y = self.rect.y + self.dy
        self.draw()

    def get_data(self):
        return self.rect, self.count, self.color
