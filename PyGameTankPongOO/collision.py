import pygame
import time


def tank_collision(obj, other_obj):
    return


def wall_collision(obj, rect):
    # print(type(obj.get_rect()), type(rect))
    # print("player cood", obj.get_rect())
    # print("wall cood", rect)
    if obj.get_rect().colliderect(rect):

        if abs(rect.bottom - obj.get_rect().top) < 15:
            obj.set_top_collision(True)
            obj.moveBottom()
            obj.set_top_collision(False)
            # print("collide TOP")

        if abs(obj.get_rect().bottom - rect.top) < 15:
            obj.set_bottom_collision(True)
            obj.moveTop()

            obj.set_bottom_collision(False)
            # print("collide bottom", obj.get_rect().bottom - rect.top)
        if abs(obj.get_rect().right - rect.left) < 15:

            obj.set_right_collision(True)
            obj.moveLeft()
            obj.set_right_collision(False)

            # print("collide right")
        if abs(obj.get_rect().left - rect.right) < 15:
            obj.set_left_collision(True)
            obj.moveRight()
            obj.set_left_collision(False)
            # print("collide left")
    else:

        obj.set_top_collision(False)
        obj.set_bottom_collision(False)
        obj.set_right_collision(False)
        obj.set_left_collision(False)
