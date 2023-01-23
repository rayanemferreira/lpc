import pygame
from config import *


def get_dx_dy(sprite_model):
    dx = 0
    dy = 0

    if sprite_model == 0:
        dy = -3
    elif sprite_model == 1:
        dx = -1
        dy = -3
    elif sprite_model == 2:
        dx = -2
        dy = -3
    elif sprite_model == 3:
        dx = -3
        dy = -3
    elif sprite_model == 4:
        dx = -3
        dy = -2
    elif sprite_model == 5:
        dx = -3
        dy = -1
    elif sprite_model == 6:
        dx = -3
    elif sprite_model == 7:
        dx = -3
        dy = 1
    elif sprite_model == 8:
        dx = -3
        dy = 2
    elif sprite_model == 9:
        dx = -3
        dy = 3
    elif sprite_model == 10:
        dx = -2
        dy = 3
    elif sprite_model == 11:
        dx = -1
        dy = 3
    elif sprite_model == 12:
        dy = 3
    elif sprite_model == 13:
        dx = 1
        dy = 3
    elif sprite_model == 14:
        dx = 2
        dy = 3
    elif sprite_model == 15:
        dx = 3
        dy = 3
    elif sprite_model == 16:
        dx = 3
        dy = 2
    elif sprite_model == 17:
        dx = 3
        dy = 1
    elif sprite_model == 18:
        dx = 3
    elif sprite_model == 19:
        dx = 3
        dy = -1
    elif sprite_model == 20:
        dx = 3
        dy = -2
    elif sprite_model == 21:
        dx = 3
        dy = -3
    elif sprite_model == 22:
        dx = 2
        dy = -3
    elif sprite_model == 23:
        dx = 1
        dy = -3
    return dx, dy


def generate_sprites(tank, tank_list):
    count = 0

    for _ in range(24):
        tank_list.append(f'img/tank_rotations/tank{tank}/tank{tank}_{count}.png')
        count = count + 15
