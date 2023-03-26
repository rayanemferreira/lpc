import math
import pygame
import sys

pygame.init()


# SPRITES
sprites_player_2 = []
sprites_player_1 = []


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


def generate_sprites(tank, tankList):
    count = 0

    for i in range(24):
        tankList.append(f'img/tank_rotations/tank{tank}/tank{tank}_{count}.png')
        count = count + 15


COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)

# screen
size = (1280, 720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Tank - PyGame Edition - 2023-15-01")

# score text cria a variável da pontuação dos jogadores
score_font = pygame.font.Font("PressStart2P.ttf", 44)
score_text = score_font.render('00 x 00', True, COLOR_WHITE, COLOR_BLACK)
score_text_rect = score_text.get_rect()
score_text_rect.center = (380, 50)

# victory text cria a variável que mostra que o jogador perdeu
victory_font = pygame.font.Font("PressStart2P.ttf", 100)
victory_text = victory_font.render('YOU LOSE', True, COLOR_WHITE, COLOR_BLACK)
victory_text_rect = score_text.get_rect()
victory_text_rect.center = (450, 300)

# sound effects
bounce_sound_effect = pygame.mixer.Sound('bounce.wav')
scoring_sound_effect = pygame.mixer.Sound('258020__kodack__arcade-bleep-sound.wav')


# player_2 1
player_2 = pygame.image.load("tank1.png")
width = player_2.get_width() // 1.2
height = player_2.get_height() // 1.2
player_2 = pygame.transform.scale(player_2, (width, height)).convert_alpha()

PLAYER_WIDTH = 40
PLAYER_HEIGHT = 40
player_2_x = 900
player_2_y = 340

player_2_dx = 4
player_2_dy = 3


generate_sprites('1', sprites_player_2)

generate_sprites('2', sprites_player_1)

image = pygame.image.load(sprites_player_2[6]).convert_alpha()

rect = image.get_rect(center=(700, 300))


player_1_x = 400
player_1_y = 340

player_1_dx = 4
player_1_dy = 3

player_1 = pygame.image.load("tank2.png")

width = player_1.get_width() // 1.2
height = player_1.get_height() // 1.2
player_1 = pygame.transform.scale(player_1, (width, height)).convert_alpha()

pygame.mouse.set_visible(False)

# ball
BALL_DIAMETER = 8
ball_player_2 = pygame.image.load("ball.png")
ball_hit = 1
ball_player_2_x = 800
ball_player_2_y = 800
ball_player_2_dx = -4
ball_player_2_dy = 0
sprite_model_player_2 = 6


ball_player_1 = pygame.image.load("ball.png")
ball_player_1_hit = 1
ball_player_1_x = 800
ball_player_1_y = 800
ball_player_1_dx = 4
ball_player_1_dy = -1
sprite_model_player_1 = 18


speed_level = 0

# lives_player_2 and score
lives_player_2 = 3
score = 0

lives_player_1 = 3

# game loop
game_loop = True
game_clock = pygame.time.Clock()

# blocks cria uma lista com imagens dos blocos
BLOCK_WIDTH = 13
BLOCK_HEIGHT = 20
colors = [pygame.image.load("block" + str(i) + ".png") for i in range(4)]

# calcula e retorna a coodenada

BORDER_WIDTH = 100
player_2_cont_vezes_que_a_bola_recocheteou = 0
player_1_cont_vezes_que_a_bola_recocheteou = 0

player_2_atirou = False
player_1_atirou = False


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
    x = pos[0]*BLOCK_WIDTH+(1280-BLOCK_WIDTH*14)/2
    y = 250-pos[1]*BLOCK_HEIGHT
    return x, y


board = '3'
try:
    board = sys.argv[1]
except:
    print(board)

blocks = create_board('boards/board'+board+".txt")

while game_loop:

    # verifica se o jogo acabou
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop = False

    # checking the victory condition
    if lives_player_2 > 0 and lives_player_1 > 0:

        # clear screen desenha tela preta
        screen.fill(COLOR_BLACK)

        # ball collision with the wall
        # verifica se a bola do player 1 bateu nas paredes
        # parede de direita
        if ball_player_2_x > 1280 - BORDER_WIDTH - BALL_DIAMETER:
            ball_player_2_x = 1280 - BORDER_WIDTH - BALL_DIAMETER
            ball_player_2_dx *= -1
            bounce_sound_effect.play()
            ball_hit = 1
            player_2_cont_vezes_que_a_bola_recocheteou += 1
        # parede de esquerda
        elif ball_player_2_x <= BORDER_WIDTH:
            ball_player_2_x = BORDER_WIDTH
            ball_player_2_dx *= -1
            bounce_sound_effect.play()
            ball_hit = 1
            player_2_cont_vezes_que_a_bola_recocheteou += 1

        # parede de cima
        if ball_player_2_y < 0:
            ball_player_2_y = 0
            ball_player_2_dy *= -1
            ball_hit = 1
            player_2_cont_vezes_que_a_bola_recocheteou += 1
        # parede de baixo
        if ball_player_2_y > 700:
            ball_player_2_dy *= -1
            player_2_cont_vezes_que_a_bola_recocheteou += 1

        # verifica se a bola do player 2 bateu no tank do player 1
        if player_2_y + PLAYER_HEIGHT > ball_player_1_y > player_2_y - PLAYER_HEIGHT:
            if player_2_x + PLAYER_WIDTH > ball_player_1_x > player_2_x - PLAYER_WIDTH:
                lives_player_2 -= 1
                player_2_x, player_2_y = 100, 100
                # faz a bola desaparecer

                player_1_cont_vezes_que_a_bola_recocheteou = 5

      # faz a bola desaparecer
        if (player_2_cont_vezes_que_a_bola_recocheteou == 5):
            ball_player_2_x = 800
            ball_player_2_y = 800
            player_2_cont_vezes_que_a_bola_recocheteou = 0
            player_2_atirou = False
            scoring_sound_effect.play()

      # ball collision with the wall
        # verifica se a bola do player 2 bateu nas paredes
        # parede de direita
        if ball_player_1_x > 1280 - BORDER_WIDTH - BALL_DIAMETER:
            ball_player_1_x = 1280 - BORDER_WIDTH - BALL_DIAMETER
            ball_player_1_dx *= -1
            bounce_sound_effect.play()
            ball_player_1_hit = 1
            player_1_cont_vezes_que_a_bola_recocheteou += 1
        # parede de esquerda
        elif ball_player_1_x <= BORDER_WIDTH:
            ball_player_1_x = BORDER_WIDTH
            ball_player_1_dx *= -1
            bounce_sound_effect.play()
            ball_player_1_hit = 1
            player_1_cont_vezes_que_a_bola_recocheteou += 1

            # parede de cima
            if ball_player_1_y < 0:
                ball_player_1_y = 0
                ball_player_1_dy *= -1
                ball_player_1_hit = 1
                player_1_cont_vezes_que_a_bola_recocheteou += 1
            # parede de baixo
            if ball_player_1_y > 700:
                ball_player_1_dy *= -1
                player_1_cont_vezes_que_a_bola_recocheteou += 1

        # verifica se a bola do player 1 bateu no tank do player 2
        if player_1_y + PLAYER_HEIGHT > ball_player_2_y > player_1_y - PLAYER_HEIGHT:
            if player_1_x + PLAYER_WIDTH > ball_player_2_x > player_1_x - PLAYER_WIDTH:
                lives_player_1 -= 1
                player_1_x, player_1_y = 100, 100
                # faz a bola desaparecer
                player_2_cont_vezes_que_a_bola_recocheteou = 5

        # faz a bola desaparecer
        if (player_1_cont_vezes_que_a_bola_recocheteou == 5):
            ball_player_1_x = 800
            ball_player_1_y = 800
            player_1_cont_vezes_que_a_bola_recocheteou = 0
            player_1_atirou = False
            scoring_sound_effect.play()

        # player_2 movement
        keys = {
            "up": pygame.K_UP,
            "left": pygame.K_LEFT,
            "right": pygame.K_RIGHT,
            "shot": pygame.K_t
        }

        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[keys["right"]] or pressed_keys[keys["left"]]:

            if pressed_keys[keys["right"]]:
                sprite_model_player_2 -= 1
            else:
                sprite_model_player_2 += 1

            if pressed_keys[keys["right"]]:
                if sprite_model_player_2 < 0:
                    sprite_model_player_2 = 23
            else:
                if sprite_model_player_2 > 23:
                    sprite_model_player_2 = 0

            player_2 = pygame.image.load(sprites_player_2[sprite_model_player_2]).convert_alpha()
            width = player_2.get_width() // 1.2
            height = player_2.get_height() // 1.2
            player_2 = pygame.transform.scale(player_2, (width, height)).convert_alpha()

        if pressed_keys[keys["up"]]:
            dx, dy = get_dx_dy(sprite_model_player_2)
            player_2_x = player_2_x + dx
            player_2_y = player_2_y + dy

        if pressed_keys[keys["shot"]]:
            dx, dy = get_dx_dy(sprite_model_player_2)
            player_2_atirou = True
            ball_player_2_dx = dx
            ball_player_2_dy = dy
            ball_player_2_x = player_2_x + 15
            ball_player_2_y = player_2_y + 20
        # player_1 movement

        keys2 = {
            "up": pygame.K_w,
            "left": pygame.K_a,
            "right": pygame.K_d,
            "shot": pygame.K_f

        }

        if pressed_keys[keys2["right"]] or pressed_keys[keys2["left"]]:

            if pressed_keys[keys2["right"]]:
                sprite_model_player_1 -= 1
            else:
                sprite_model_player_1 += 1

            if pressed_keys[keys2["right"]]:
                if sprite_model_player_1 < 0:
                    sprite_model_player_1 = 23
            else:
                if sprite_model_player_1 > 23:
                    sprite_model_player_1 = 0

            player_1 = pygame.image.load(sprites_player_1[sprite_model_player_1]).convert_alpha()
            width = player_1.get_width() // 1.2
            height = player_1.get_height() // 1.2
            player_1 = pygame.transform.scale(player_1, (width, height)).convert_alpha()

        if pressed_keys[keys2["up"]]:
            dx, dy = get_dx_dy(sprite_model_player_1)
            player_1_x = player_1_x + dx
            player_1_y = player_1_y + dy

        if pressed_keys[keys2["shot"]]:
            dx, dy = get_dx_dy(sprite_model_player_1)
            player_1_atirou = True
            ball_player_1_dx = dx
            ball_player_1_dy = dy
            ball_player_1_x = player_1_x + 25
            ball_player_1_y = player_1_y + 17

        score_text = score_font.render(
            "LIVES P1:" + str(lives_player_1) + "| LIVES P2:" + str(lives_player_2),
            True, COLOR_WHITE, COLOR_BLACK)

        if (player_2_atirou):
            # ball movement
            ball_player_2_x = ball_player_2_x + ball_player_2_dx
            ball_player_2_y = ball_player_2_y + ball_player_2_dy

        if (player_1_atirou):
            # ball movement
            ball_player_1_x = ball_player_1_x + ball_player_1_dx
            ball_player_1_y = ball_player_1_y + ball_player_1_dy

        # drawing objects
        # renderiza / desenha a bola os players e os blocos na tela
        screen.blit(ball_player_2, (ball_player_2_x, ball_player_2_y))

        screen.blit(ball_player_1, (ball_player_1_x, ball_player_1_y))

        screen.blit(player_2, (player_2_x, player_2_y))

        screen.blit(player_1, (player_1_x, player_1_y))

        screen.blit(score_text, score_text_rect)
        for i in range(len(blocks)):
            for block in blocks[i]:
                screen.blit(colors[1], block)
    else:
        # mostra que o jogador venceu
        if lives_player_1 > 0:
            victory_text = victory_font.render('P1 WIN', True, COLOR_WHITE, COLOR_BLACK)
        else:
            victory_text = victory_font.render('P2 WIN', True, COLOR_WHITE, COLOR_BLACK)

        screen.fill(COLOR_BLACK)
        screen.blit(victory_text, victory_text_rect)

    # update screen
    pygame.display.flip()
    game_clock.tick(55)

pygame.quit()
