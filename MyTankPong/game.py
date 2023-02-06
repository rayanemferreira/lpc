import pygame.mixer

from tank import Tank
from config import *
from score import Score

pygame.init()
pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]


class Game:
    pygame.mixer.init()

    def __init__(self):
        self.game_loop = True
        self.clock = pygame.time.Clock()

        self.player1_rect = pygame.Rect(80, 375, 40, 40)
        self.player2_rect = pygame.Rect(1160, 375, 40, 40)
        self.player3_rect = pygame.Rect(400, 600, 40, 40)
        self.player4_rect = pygame.Rect(600, 150, 40, 40)

        self.score_a = self.score_b = 0
        self.score_c = self.score_d = 0

        self.bullets = []

        self.tank_1 = Tank(0, self.player1_rect, "sprites/player1.png", RED)
        self.tank_2 = Tank(180, self.player2_rect, "sprites/player2.png", BLUE)
        self.tank_3 = Tank(150, self.player3_rect, "sprites/player3.png", GREEN)
        self.tank_4 = Tank(150, self.player4_rect, "sprites/player4.png", BLACK)

        self.sound_explosion = pygame.mixer.Sound("sound/explosion.mp3")
        self.sound_explosion.set_volume(0.5)

    def updateScoreByColor(self, color, b, score_1, score_2, score_3, score_4):

        if (color == BLUE):
            self.score_a += 1
            score_1.upload_score(self.score_a)
            self.bullets.remove(b)

        if (color == RED):
            print('red')
            self.score_b += 1
            score_2.upload_score(self.score_b)
            self.bullets.remove(b)

        if (color == GREEN):
            print('GREEN')

            self.score_c += 1
            score_3.upload_score(self.score_c)
            self.bullets.remove(b)

        if (color == BLACK):
            print('black')

            self.score_d += 1
            score_4.upload_score(self.score_d)
            self.bullets.remove(b)

    def run(self):
        self.clock.tick(60)

        score_1 = Score(self.score_b, 980, BLUE)

        score_2 = Score(self.score_a, 300, RED)

        score_3 = Score(self.score_c, 780, GREEN)

        score_4 = Score(self.score_d, 450, BLACK)

        while self.game_loop:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_loop = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.game_loop = False
                    if event.key == pygame.K_s:
                        self.bullets.append(self.tank_1.shot_bullet())
                    if event.key == pygame.K_DOWN:
                        self.bullets.append(self.tank_2.shot_bullet())

                    if event.key == pygame.K_k:
                        self.bullets.append(self.tank_3.shot_bullet())

                    if event.key == pygame.K_g:
                        self.bullets.append(self.tank_4.shot_bullet())

                if event.type == pygame.JOYBUTTONDOWN:
                    if event.button == 0:
                        self.bullets.append(self.tank_1.shot_bullet())

                if event.type == pygame.JOYHATMOTION:
                    print(event)
                    if event.value[0] == 1:
                        self.tank_1.joy_move(1, 0, 0)
                    if event.value[0] == -1:
                        self.tank_1.joy_move(-1, 0, 0)
                    if event.value[1] == 1:
                        self.tank_1.joy_move(0, 1, 1)

            keys = pygame.key.get_pressed()

            # Move p1
            self.tank_1.control(keys, [pygame.K_w, pygame.K_a, pygame.K_d], 0)
            self.tank_1.control(keys, [pygame.K_w, pygame.K_a, pygame.K_d], 0)
            self.tank_1.draw()
            # Move p2
            self.tank_2.control(keys, [pygame.K_UP, pygame.K_LEFT, pygame.K_RIGHT], 1)
            self.tank_2.draw()

            # Move p3
            self.tank_3.control(keys, [pygame.K_i, pygame.K_j, pygame.K_l], 1)
            self.tank_3.draw()

            # Move p4
            self.tank_4.control(keys, [pygame.K_t, pygame.K_f, pygame.K_h], 1)
            self.tank_4.draw()

            # start shot
            for b in self.bullets:
                b.move()

                response_1, color_1 = self.tank_1.player_death(b.get_data())
                response_2, color_2 = self.tank_2.player_death(b.get_data())
                response_3, color_3 = self.tank_3.player_death(b.get_data())
                response_4, color_4 = self.tank_4.player_death(b.get_data())

                if b.get_data()[0] == -40:
                    self.bullets.remove(b)

                elif response_1:
                    print('color_1', color_1)
                    pygame.mixer.Channel(4).play(self.sound_explosion)
                    self.updateScoreByColor(color_1, b, score_1, score_2, score_3, score_4)

                elif response_2:
                    print('color_2', color_2)
                    pygame.mixer.Channel(4).play(self.sound_explosion)
                    self.updateScoreByColor(color_2, b, score_1, score_2, score_3, score_4)

                elif response_3:
                    print('color_3', color_3)
                    pygame.mixer.Channel(4).play(self.sound_explosion)
                    self.updateScoreByColor(color_3, b, score_1, score_2, score_3, score_4)

                elif response_4:
                    print('color_4', color_4)
                    pygame.mixer.Channel(4).play(self.sound_explosion)
                    self.updateScoreByColor(color_4, b, score_1, score_2, score_3, score_4)

            score_1.draw(screen)
            score_2.draw(screen)

            score_3.draw(screen)
            score_4.draw(screen)

            pygame.display.update()
            screen.fill("#641E0A")


game = Game()
game.run()
