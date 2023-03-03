import pygame
from collision import collision_ball
from tank import Tank
from config import *
from score import Score
from ball import Ball
import math
from config import score_song, shot_song, end_game_song
pygame.init()


class Game:
    pygame.mixer.init()

    def __init__(self):

        self.ball = Ball(625, 363, 50, 50)
        self.willPlayEndSound = True
        self.game_loop = True
        self.clock = pygame.time.Clock()

        self.player1_rect = pygame.Rect(125, 363, 80, 80)
        self.player2_rect = pygame.Rect(1120, 363, 80, 80)
        self.score_a = self.score_b = 0
        self.bullets = []
        self.tank_1 = Tank(0, self.player1_rect, "sprites/nave-1.png", RED)
        self.tank_2 = Tank(180, self.player2_rect, "sprites/nave-2.png", GREEN)

    def playEndSound(self):
        if (self.willPlayEndSound):
            end_game_song.play()
            self.willPlayEndSound = False

    def showVictoryText(self, player_num):
        self.victory_font = pygame.font.Font('assets/PressStart2P.ttf', 44)
        self.victory_text = self.victory_font.render('', True, WHITE, BLACK)
        self.victory_text_rect = self.victory_text.get_rect()
        self.victory_text_rect.center = (700, 300)
        Score.center = (550, 400)
        victory_text = self.victory_font.render('P{} WINS!'.format(player_num), True, WHITE, BLACK)
        screen.fill(BLACK)
        screen.blit(victory_text, self.victory_text_rect)

    def finalizeGame(self):
        self.ball.hide()
        self.playEndSound()
        if self.score_a > self.score_b:
            self.showVictoryText(2)
        else:
            self.showVictoryText(1)

    def run(self):
        self.clock.tick(100)

        score_1 = Score(self.score_a, 980, GREEN)
        score_2 = Score(self.score_b, 300, RED)

        while self.game_loop:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_loop = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.game_loop = False
                    if event.key == pygame.K_s and len(self.bullets) == 0:
                        self.bullets.append(self.tank_1.shot_bullet())
                        shot_song.play()
                    if event.key == pygame.K_DOWN and len(self.bullets) == 0:
                        self.bullets.append(self.tank_2.shot_bullet())
                        shot_song.play()

            if (self.score_a == 5 or self.score_b == 5):
                self.finalizeGame()

            else:

                keys = pygame.key.get_pressed()

                # Move p1
                self.tank_1.control(keys, [pygame.K_w, pygame.K_a, pygame.K_d], 0)
                self.tank_1.draw()
                # Move p2
                self.tank_2.control(keys, [pygame.K_UP, pygame.K_LEFT, pygame.K_RIGHT], 1)
                self.tank_2.draw()

                if collision_ball(self.tank_1.rect, self.ball.get_rect(), self.tank_1.ang):
                    self.ball.dx += math.cos(math.radians(self.tank_1.ang))
                    self.ball.dy -= math.sin(math.radians(self.tank_1.ang))

                if collision_ball(self.tank_2.rect, self.ball.get_rect(), self.tank_2.ang):
                    self.ball.dx += math.cos(math.radians(self.tank_2.ang))
                    self.ball.dy -= math.sin(math.radians(self.tank_2.ang))
                # start shot
                for b in self.bullets:
                    b.move()
                    if b.get_data()[0].x <= -50:
                        self.bullets.remove(b)
                    if self.ball.detection_collision(b):
                        self.bullets.remove(b)

                if self.ball.get_rect().colliderect(20, 277, 80, 220):
                    self.score_a += 1
                    self.ball.restart()
                    score_song.play()
                    score_1.upload_score(self.score_a)
                    self.bullets.clear()

                if self.ball.get_rect().colliderect((1200, 277, 80, 220)):
                    self.score_b += 1
                    self.ball.restart()
                    score_song.play()
                    score_2.upload_score(self.score_b)
                    self.bullets.clear()

            score_1.draw(screen)
            score_2.draw(screen)
            self.ball.move()
            pygame.display.update()
            screen.fill("#1d982b")


game = Game()
game.run()
