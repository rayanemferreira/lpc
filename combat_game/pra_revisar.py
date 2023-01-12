import math
import pygame

pygame.init()

COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)

# screen
size = (1280, 720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Breakout - PyGame Edition - 2023-09-01")

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

# player 1
player = pygame.image.load("tank1.png")
PLAYER_WIDTH = 40
PLAYER_HEIGHT = 10
player_1_x = 900
player_1_y = 640

player_1_dx = 4
player_1_dy = 3

player_2_x = 90
player_2_y = 60

player_2_dx = 4
player_2_dy = 3

player2 = pygame.image.load("tank2.png")
player_y2 = 400

pygame.mouse.set_visible(False)

# ball
ball = pygame.image.load("ball.png")
ball_hit = 1
BALL_DIAMETER = 8
ball_x = 640
ball_y = 360
ball_dx = 4
ball_dy = 3


speed_level = 0

# lives and score
lives = 542343443434423
score = 0

# game loop
game_loop = True
game_clock = pygame.time.Clock()

# blocks cria uma lista com imagens dos blocos
BLOCK_WIDTH = 40
BLOCK_HEIGHT = 10
colors = [pygame.image.load("block" + str(i) + ".png") for i in range(4)]

# calcula e retorna a coodenada


def block_pos(pos):
    x = pos[0]*BLOCK_WIDTH+(1280-BLOCK_WIDTH*14)/2
    y = 250-pos[1]*BLOCK_HEIGHT
    return x, y


# blocks cria uma lista com as coordenadas x e y dos blocos
# gera os blocos
blocks = [[block_pos((i, j)) for i in range(14)] for j in range(8)]

BORDER_WIDTH = (1280-BLOCK_WIDTH*14)/2

while game_loop:

    # verifica se o jogo acabou
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop = False

    # checking the victory condition
    if lives > 0 & score < 4480:

        # clear screen desenha tela preta
        screen.fill(COLOR_BLACK)

        # ball collision with the wall
        # verifica se a bola bateu nas paredes
        if ball_x > 1280 - BORDER_WIDTH - BALL_DIAMETER:
            ball_x = 1280 - BORDER_WIDTH - BALL_DIAMETER
            ball_dx *= -1
            bounce_sound_effect.play()
            ball_hit = 1
        elif ball_x <= BORDER_WIDTH:
            ball_x = BORDER_WIDTH
            ball_dx *= -1
            bounce_sound_effect.play()
            ball_hit = 1
        if ball_y < 0:
            ball_y = 0
            ball_dy *= -1
            ball_hit = 1

        # ball collision with the player's paddle
        # verifica se a bola bateu no paddle
        # if 665 > ball_y > 655-PLAYER_HEIGHT:
        #     if player_y < ball_x + BALL_DIAMETER/2 < player_y + PLAYER_WIDTH:
        #         ball_y = 655-PLAYER_HEIGHT
        #         ball_dy *= -1
        #         sign = 1
        #         if (ball_x+BALL_DIAMETER/2-(player_y+PLAYER_WIDTH/2))/7 < 0:
        #             sign = -1
        #         ball_dx = ((ball_x+BALL_DIAMETER/2-(player_y+PLAYER_WIDTH/2))/7+sign)*(1+speed_level/4)
        #         bounce_sound_effect.play()
        #         ball_hit = 1

        # ball collision with blocks
        # verifica se a bola bateu nos blocos e remove o bloco que foi atingido
        if ball_hit:
            for i in range(len(blocks)):
                for block in blocks[i]:
                    if block[1]+BLOCK_HEIGHT > ball_y > block[1]:
                        if block[0] < ball_x + 10 < block[0] + BLOCK_WIDTH:
                            sign = 1
                            if ball_dy < 0:
                                sign = -1
                            if math.floor(i / 2) > speed_level:
                                speed_level = math.floor(i / 2)
                            ball_dy = (3 + speed_level)*sign
                            ball_dy *= -1
                            blocks[i].remove(block)
                            score += 10 + math.floor(i / 2) * 20
                            bounce_sound_effect.play()
                            ball_hit = 0

        # losing lives
        # verifica se o jogador morreu
        if ball_y > 800:
            ball_x = 640
            ball_y = 360
            ball_dy *= -1
            ball_dx *= -1
            lives -= 1
            ball_hit = 1
            speed_level = 0
            scoring_sound_effect.play()

        # ball movement
        ball_x = ball_x + ball_dx
        ball_y = ball_y + ball_dy
        keys = {
            "up": pygame.K_UP,
            "down": pygame.K_DOWN,
            "left": pygame.K_LEFT,
            "right": pygame.K_RIGHT
        }
        # player movement

        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[keys["right"]] or pressed_keys[keys["left"]]:
            if pressed_keys[keys["right"]]:
                player_1_dx = +1
                player_1_x = player_1_x + player_1_dx
            else:
                player_1_dx = -1
                player_1_x = player_1_x + player_1_dx

        if pressed_keys[keys["up"]] or pressed_keys[keys["down"]]:
            if pressed_keys[keys["up"]]:
                player_1_dy = -1
                player_1_y = player_1_y + player_1_dy
            else:
                player_1_dy = +1
                player_1_y = player_1_y + player_1_dy

        keys2 = {
            "up": pygame.K_w,
            "down": pygame.K_s,
            "left": pygame.K_a,
            "right": pygame.K_d
        }

        if pressed_keys[keys2["right"]] or pressed_keys[keys2["left"]]:
            if pressed_keys[keys2["right"]]:
                player_2_dx = +1
                player_2_x = player_2_x + player_2_dx
            else:
                player_2_dx = -1
                player_2_x = player_2_x + player_2_dx

        if pressed_keys[keys2["up"]] or pressed_keys[keys2["down"]]:
            if pressed_keys[keys2["up"]]:
                player_2_dy = -1
                player_2_y = player_2_y + player_2_dy
            else:
                player_2_dy = +1
                player_2_y = player_2_y + player_2_dy

        # força o paddle a ficar dentro do tabuleiro
        # player 1 collides with right wall
        # if player_y <= BORDER_WIDTH:
        #     player_y = BORDER_WIDTH
        # # player 1 collides with left wall
        # elif player_y >= 1280-BORDER_WIDTH-PLAYER_WIDTH:
        #     player_y = 1280-BORDER_WIDTH-PLAYER_WIDTH

        # update score hud
        # atualiza os textos de vidas e score
        score_text = score_font.render("LIVES: " + str(lives) + " | SCORE: " + str(score), True, COLOR_WHITE,
                                       COLOR_BLACK)

        # drawing objects
        # renderiza / desenha a bola o paddle e os blocos na tela
        screen.blit(ball, (ball_x, ball_y))
        screen.blit(player, (player_1_x, player_1_y))

        screen.blit(player2, (player_2_x, player_2_y))

        screen.blit(score_text, score_text_rect)
        for i in range(len(blocks)):
            for block in blocks[i]:
                screen.blit(colors[math.floor(i/2)], block)
    else:
        # drawing victory
        # mostra que o jogador venceu
        score_text_rect.center = (600, 450)
        if score >= 4480:
            victory_text = victory_font.render('YOU WIN', True, COLOR_WHITE, COLOR_BLACK)
        screen.fill(COLOR_BLACK)
        score_text = score_font.render("SCORE: " + str(score), True, COLOR_WHITE,
                                       COLOR_BLACK)
        screen.blit(score_text, score_text_rect)
        screen.blit(victory_text, victory_text_rect)

    # update screen
    pygame.display.flip()
    game_clock.tick(55)

pygame.quit()
