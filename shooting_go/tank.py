import math

from config import *
from bullet import Bullet
from collision import tank1_collision_objects, tank2_collision_objects


class Tank:
    def __init__(self, ang, rect, image, color_bullet):
        self.ang = ang
        self.w = rect.w
        self.h = rect.h
        self.coordinates = [rect.x, rect.y]
        self.image = pygame.image.load(image)
        self.surface = pygame.transform.scale(self.image, (self.w, self.h))
        self.rotated = pygame.transform.rotate(self.image, self.ang)
        self.rect = self.image.get_rect(center=(self.coordinates[0] + self.w / 2, self.coordinates[1] + self.h / 2))
        self.bullets = 0
        self.count = 0
        self.color_bullet = color_bullet
        self.per = [True, True]

    def permission(self):
        # players collide with objects
        self.per[0] = tank1_collision_objects(self.rect, self.ang)
        self.per[1] = tank2_collision_objects(self.rect, self.ang)

    def shot_bullet(self):
        self.bullets = Bullet(self.coordinates[0], self.coordinates[1], self.ang, self.color_bullet)
        return self.bullets

    def move(self, keys, player_keys, permission):
        if keys[player_keys[0]] and permission:
            self.coordinates[0] += math.cos(math.radians(self.ang))
            self.coordinates[1] -= math.sin(math.radians(self.ang))
            self.draw()

        elif keys[player_keys[1]]:
            self.ang += 1
            self.draw()

        elif keys[player_keys[2]]:
            self.ang += -1
            self.draw()

    def control(self, keys, touch_keys, per):
        self.permission()
        self.move(keys, touch_keys, self.per[per])

    def draw(self):
        self.surface = pygame.transform.scale(self.surface, (self.w, self.h))
        self.rotated = pygame.transform.rotate(self.surface, self.ang)
        self.rect = self.rotated.get_rect(center=(self.coordinates[0] + 25, self.coordinates[1] + 25))
        screen.blit(self.rotated, self.rect)
