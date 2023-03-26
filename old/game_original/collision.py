from config import *
import math


def load_images(sprite, ang, w, h, xp, yp, image):
    sprite.image = pygame.image.load(image)
    sprite.image = pygame.transform.scale(sprite.image, (w, h))
    sprite.image = pygame.transform.rotate(sprite.image, ang)
    sprite.rect = sprite.image.get_rect(center=(xp + 40, yp + 40))


def detection_collision(player):
    rect = arena.draw_object()
    detection = []
    for x in rect:
        detection.append(x.colliderect(player))
    if True in detection:
        return False
    else:
        return True


def tank1_collision_objects(rect, angle):
    # players collide with objects
    collision_1 = pygame.sprite.Sprite()
    load_images(collision_1, angle, 10, 60,
                rect.x + 20 * math.cos(math.radians(-angle)),
                rect.y + 20 * math.sin(math.radians(-angle)), "sprites/collision_object.png")
    if detection_collision(collision_1):
        per_1 = True
    else:
        per_1 = False

    return per_1


def tank2_collision_objects(rect, angle):
    collision_2 = pygame.sprite.Sprite()
    load_images(collision_2, angle, 10, 50, rect.x - 30 * math.sin(math.radians(angle - 90)),
                rect.y - 30 * math.cos(math.radians(angle - 90)), "sprites/collision_object.png")

    # collision player 2 with objects
    if detection_collision(collision_2):
        per_2 = True
    else:
        per_2 = False

    return per_2
