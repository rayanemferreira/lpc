from config import *
from bullet import Bullet
from collision import tank1_collision_objects, tank2_collision_objects
import math


class Tank:
    def __init__(self, ang, rect, image, color_bullet):
        self.ang = ang
        self.w = rect.w
        self.h = rect.h
        self.coordinates = [rect.x, rect.y]
        self.image = pygame.image.load(image)
        self.surface = pygame.transform.scale(self.image, (self.w, self.h))
        self.rotated = pygame.transform.rotate(self.image, self.ang)
        self.rect = self.image.get_rect()
        self.bullets = 0
        self.count = 0
        self.color_bullet = color_bullet
        self.per = [True, True]
        self.sound_shot = pygame.mixer.Sound("sound/shot.mp3")
        self.sound_move = pygame.mixer.Sound("sound/move.mp3")
        self.sound_move.set_volume(0.5)

    def permission(self):
        self.per[0] = tank1_collision_objects(self.rect, self.ang)
        self.per[1] = tank2_collision_objects(self.rect, self.ang)

    def shot_bullet(self):
        self.bullets = Bullet(self.coordinates[0], self.coordinates[1], self.ang, self.color_bullet)
        pygame.mixer.Channel(2).play(self.sound_shot)
        return self.bullets

    def move(self, keys, player_keys, permission):
        if keys[player_keys[0]] and permission:
            self.coordinates[0] += MOVE_SPEED * math.cos(math.radians(self.ang))
            self.coordinates[1] -= MOVE_SPEED * math.sin(math.radians(self.ang))
            pygame.mixer.Channel(1).play(self.sound_move)
            self.draw()

        elif keys[player_keys[1]]:
            self.ang += TURN_SPEED
            pygame.mixer.Channel(1).play(self.sound_move)
            self.draw()

        elif keys[player_keys[2]]:
            self.ang += -TURN_SPEED
            pygame.mixer.Channel(1).play(self.sound_move)
            self.draw()

    def joy_move(self, value_x, value_y, permission):
        if value_y == 1 and permission:
            self.coordinates[0] += MOVE_SPEED * math.cos(math.radians(self.ang))
            self.coordinates[1] -= MOVE_SPEED * math.sin(math.radians(self.ang))
            pygame.mixer.Channel(1).play(self.sound_move)
            self.draw()

        elif value_x == -1:
            self.ang += TURN_SPEED
            pygame.mixer.Channel(1).play(self.sound_move)
            self.draw()

        elif value_x == 1:
            self.ang += -TURN_SPEED
            pygame.mixer.Channel(1).play(self.sound_move)
            self.draw()

    def control(self, keys, touch_keys, per):
        self.permission()
        self.move(keys, touch_keys, self.per[per])

    def draw(self):
        self.surface = pygame.transform.scale(self.surface, (self.w, self.h))
        self.rotated = pygame.transform.rotate(self.surface, self.ang)
        self.rect = self.rotated.get_rect(center=(self.coordinates[0] + 25, self.coordinates[1] + 25))
        screen.blit(self.rotated, self.rect)

    def player_death(self, ball):
        ball, count_ball, color_bullet = ball[0], ball[1], ball[2]

        if ball.colliderect(self.rect) and color_bullet != self.color_bullet:
            self.count += 1
            count_ball += touch_limit
            ang = 1
            self.ang = 0
            death_count = 0
            while death_count <= 720:
                if death_count == 720:
                    if self.count % 2 == 0 and self.count != 0:
                        self.coordinates[1] = 100
                    elif self.count % 2 == 1 and self.count != 0:
                        self.coordinates[1] = 650

                death_count += 1
                self.ang += ang

            return True, color_bullet
        return False, None
