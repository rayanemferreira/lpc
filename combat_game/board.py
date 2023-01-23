from config import *
import sys


def create_board(board):
    field = open(board, 'r')
    global wall_list
    global not_wall_list
    wall_list = []
    not_wall_list = []
    y = -20

    for line in field:
        x = -42.0
        for block in line:
            if block == '1':
                wall_list.append(block_pos((x, y)))
            elif block == '0':
                not_wall_list.append((x, y))
            x += 1
        y += 1
    return [wall_list]


def block_pos(pos):
    x = pos[0] * block_width + (1270 - block_width * 14) / 2
    y = 270 - pos[1] * block_height
    return x, y


try:
    board = sys.argv[1]
except:
    print(board)
