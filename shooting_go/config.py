import pygame
from arena import Arena
pygame.font.init()

sc_width = 1300
sc_height = 750
screen = pygame.display.set_mode((sc_width, sc_height), pygame.FULLSCREEN)

RED = (255, 0, 0)
GREEN = (0, 255, 0)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

ang_left = 0
ang_right = 0

num_arena = 1
arena = Arena(num_arena, screen)

touch_limit = 4
bullet_limit = 3
speed_ball = 5
border = 25
pygame.mixer.init()

score_song = pygame.mixer.Sound('assets/score.mp3')
shot_song = pygame.mixer.Sound('assets/shot.wav')
end_game_song = pygame.mixer.Sound('assets/soccer_crowd.mp3')

pygame.display.set_caption("Shooting.GO")
font = pygame.font.Font("sprites/PressStart2P.ttf", 40)
