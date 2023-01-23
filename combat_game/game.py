import pygame
import random
from tank import get_dx_dy
from tank import generate_sprites
from config import *
from board import create_board


def game_start():
    pygame.init()

    # SPRITES
    sprites_player_2 = []
    sprites_player_1 = []

    # screen
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("TANK PONG")

    # score text
    score_font = pygame.font.Font("PressStart2P.ttf", 44)
    score_text = score_font.render('00 x 00', True, white, red)
    score_text_rect = score_text.get_rect()
    score_text_rect.center = (290, 50)

    # victory text
    victory_font = pygame.font.Font("PressStart2P.ttf", 100)
    victory_text = victory_font.render('YOU LOSE', True, white, red)
    victory_text_rect = score_text.get_rect()
    victory_text_rect.center = (450, 300)

    # sound effects
    bounce_sound_effect = pygame.mixer.Sound('bounce.wav')
    scoring_sound_effect = pygame.mixer.Sound('scoring.wav')

    # player_2
    player_2 = pygame.image.load("tank1.png")
    width = player_2.get_width() // 1.2
    height = player_2.get_height() // 1.2
    player_2 = pygame.transform.scale(player_2, (width, height)).convert_alpha()

    generate_sprites('1', sprites_player_2)
    generate_sprites('2', sprites_player_1)

    image = pygame.image.load(sprites_player_2[6]).convert_alpha()
    rect = image.get_rect(center=(700, 300))

    player_1 = pygame.image.load("tank2.png")

    width = player_1.get_width() // 1.2
    height = player_1.get_height() // 1.2
    player_1 = pygame.transform.scale(player_1, (width, height)).convert_alpha()

    pygame.mouse.set_visible(False)

    ball_player_2 = pygame.image.load("ball.png")
    ball_player_1 = pygame.image.load("ball.png")

    sprite_model_player_2 = 6
    sprite_model_player_1 = 18

    player_2_x = 1070
    player_2_y = 370
    player_1_x = 160
    player_1_y = 370

    # ball
    ball_diameter = 8
    ball_hit = 1
    ball_player_2_x = 800
    ball_player_2_y = 800
    ball_player_2_dx = -3
    ball_player_2_dy = 0
    sprite_model_player_2 = 6

    ball_player_1_hit = 1
    ball_player_1_x = 800
    ball_player_1_y = 800
    ball_player_1_dx = 3
    ball_player_1_dy = -1
    sprite_model_player_1 = 18

    # lives_player_2 and score
    lives_player_2 = 3
    lives_player_1 = 3

    # game loop
    game_loop = True
    game_clock = pygame.time.Clock()

    # block list
    colors = [pygame.image.load("block.png") for _ in range(4)]

    player_1_ball_hits = 0
    player_2_ball_hits = 0

    player_2_shot = False
    player_1_shot = False

    blocks = create_board('boards/board' + board + ".txt")
    cont = 0
    while game_loop:

        # quit game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_loop = False

        # checking the victory condition
        if lives_player_2 > 0 and lives_player_1 > 0:
            # ball collision with blocks

            if ball_hit:

                for i in range(len(blocks)):
                    for block in blocks[i]:
                        if cont < 0:
                            if block[1]+block_height+10 > ball_player_2_y > block[1] - 10:
                                if (block[0] - block_width < ball_player_2_x < block[0] + block_width+20):
                                    player_2_ball_hits += 1
                                    if (ball_player_2_dx >= 0 and ball_player_2_dy == 0):
                                        ball_player_2_dx *= -1

                                    elif (ball_player_2_dx < 0 and ball_player_2_dy == 0):
                                        ball_player_2_dx *= -1

                                    elif (ball_player_2_dy >= 0 and ball_player_2_dx == 0):
                                        ball_player_2_dy *= -1

                                    elif (ball_player_2_dy < 0 and ball_player_2_dx == 0):
                                        ball_player_2_dy *= -1

                                    elif (ball_player_2_dx < 0 and ball_player_2_dy > 0):
                                        ball_player_2_dy *= -1

                                    elif (ball_player_2_dy < 0 and ball_player_2_dx > 0):
                                        ball_player_2_dy *= -1

                                    elif (ball_player_2_dy > 0 and ball_player_2_dx > 0):
                                        ball_player_2_dx *= -1

                                    elif (ball_player_2_dy < 0 and ball_player_2_dx < 0):
                                        ball_player_2_dx *= -1

                                    cont = 2

                            if block[1]+block_height+10 > ball_player_1_y > block[1] - 10:
                                if (block[0] - block_width < ball_player_1_x < block[0] + block_width+20):
                                    player_1_ball_hits += 1

                                    print('ball_player_1_dx', ball_player_1_dx, ball_player_1_dy)
                                    cont = 2
                                    if (ball_player_1_dx >= 0 and ball_player_1_dy == 0):
                                        ball_player_1_dx *= -1

                                    elif (ball_player_1_dx < 0 and ball_player_1_dy == 0):
                                        ball_player_1_dx *= -1

                                    elif (ball_player_1_dy >= 0 and ball_player_1_dx == 0):
                                        ball_player_1_dy *= -1

                                    elif (ball_player_1_dy < 0 and ball_player_1_dx == 0):
                                        ball_player_1_dy *= -1

                                    elif (ball_player_1_dx < 0 and ball_player_1_dy > 0):
                                        ball_player_1_dy *= -1

                                    elif (ball_player_1_dy < 0 and ball_player_1_dx > 0):
                                        ball_player_1_dy *= -1

                                    elif (ball_player_1_dy > 0 and ball_player_1_dx > 0):
                                        ball_player_1_dx *= -1

                                    elif (ball_player_1_dy < 0 and ball_player_1_dx < 0):
                                        ball_player_1_dx *= -1

                screen.fill(red)

            # death verify (2 to 1)
            if player_2_y + player_height > ball_player_1_y > player_2_y - player_height:
                if player_2_x + player_width > ball_player_1_x > player_2_x - player_width:
                    lives_player_2 -= 1

                    player_2_x, player_2_y = random.randint(1020, 1070), random.randint(320, 370)
                    # kill ball
                    player_1_ball_hits = 5

            # # kill ball
            # if (player_2_ball_hits > 0):
            #     print('player_2_ball_hits', player_2_ball_hits)
            if player_2_ball_hits >= 5:
                ball_player_2_x = 800
                ball_player_2_y = 800
                player_2_ball_hits = 0
                player_2_shot = False
                scoring_sound_effect.play()

            # death verify (1 to 2)
            if player_1_y + player_height > ball_player_2_y > player_1_y - player_height:
                if player_1_x + player_width > ball_player_2_x > player_1_x - player_width:
                    lives_player_1 -= 1
                    player_1_x, player_1_y = random.randint(120, 160), random.randint(320, 370)
                    # kill ball
                    player_2_ball_hits = 5

            # kill ball
            if player_1_ball_hits >= 5:
                ball_player_1_x = 800
                ball_player_1_y = 800
                player_1_ball_hits = 0
                player_1_shot = False
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
                player_2_shot = True
                ball_player_2_dx = dx
                ball_player_2_dy = dy
                ball_player_2_x = player_2_x + 15
                ball_player_2_y = player_2_y + 20
                player_2_ball_hits = 0
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
                player_1_shot = True
                ball_player_1_dx = dx
                ball_player_1_dy = dy
                ball_player_1_x = player_1_x + 25
                ball_player_1_y = player_1_y + 17
                player_1_ball_hits = 0

            score_text = score_font.render(
                "LIVES P1:" + str(lives_player_1) + " | LIVES P2:" + str(lives_player_2),
                True, white, red)

            if player_2_shot:
                # ball movement
                ball_player_2_x = ball_player_2_x + ball_player_2_dx
                ball_player_2_y = ball_player_2_y + ball_player_2_dy

            if player_1_shot:
                # ball movement
                ball_player_1_x = ball_player_1_x + ball_player_1_dx
                ball_player_1_y = ball_player_1_y + ball_player_1_dy

            # drawing objects
            screen.blit(ball_player_2, (ball_player_2_x, ball_player_2_y))
            screen.blit(ball_player_1, (ball_player_1_x, ball_player_1_y))
            screen.blit(player_2, (player_2_x, player_2_y))
            screen.blit(player_1, (player_1_x, player_1_y))
            screen.blit(score_text, score_text_rect)

            for i in range(len(blocks)):
                for block in blocks[i]:
                    screen.blit(colors[1], block)

            cont += -1

        else:
            # show player victory
            if lives_player_1 > 0:
                victory_text = victory_font.render('P1 WIN', True, white, red)
            else:
                victory_text = victory_font.render('P2 WIN', True, white, red)

            screen.fill(red)
            screen.blit(victory_text, victory_text_rect)

        # update screen
        pygame.display.flip()
        game_clock.tick(fps)

    pygame.quit()
