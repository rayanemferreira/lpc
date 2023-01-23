import pygame


for block in blocks:
    if player_1.rect.colliderect(block):
        if abs(player_1.rect.top - block.rect.bottom):
            return player_1_x, player_1_y + 1
        if abs(player_1.rect.bottom - block.rect.top):
            return player_1_x, player_1_y - 1
        if abs(player_1.rect.left - block.rect.right):
            return player_1_x - 1, player_1_y
        if abs(player_1.rect.right - block.rect.left):
            return player_1_x + 1, player_1_y
