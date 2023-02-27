import pygame
from collision import collision_ball
from tank import Tank
from config import *
from score import Score
from ball import Ball
import math

pygame.init()


class Game:
    pygame.mixer.init()

    def __init__(self):
        self.score_song = pygame.mixer.Sound('assets/score.mp3')
        self.shot_song = pygame.mixer.Sound('assets/shot.wav')
        self.end_game_song = pygame.mixer.Sound('assets/soccer_crowd.mp3')

        self.game_loop = True
        self.clock = pygame.time.Clock()

        self.player1_rect = pygame.Rect(125, 363, 80, 80)
        self.player2_rect = pygame.Rect(1120, 363, 80, 80)
        self.score_a = self.score_b = 0
        self.bullets = []
        self.tank_1 = Tank(0, self.player1_rect, "sprites/nave-1.png", RED)
        self.tank_2 = Tank(180, self.player2_rect, "sprites/nave-2.png", GREEN)

    def run(self):
        self.clock.tick(100)

        score_1 = Score(self.score_a, 980, GREEN)
        score_2 = Score(self.score_b, 300, RED)

        self.victory_font = pygame.font.Font('assets/PressStart2P.ttf', 44)
        self.score_text = self.victory_font.render('00 x 00', True, WHITE, BLACK)
        self.victory_text_rect = self.score_text.get_rect()
        self.victory_text_rect.center = (700, 300)
        ball = Ball(625, 363, 50, 50)
        self.play_end_game = True

        while self.game_loop:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_loop = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.game_loop = False
                    if event.key == pygame.K_s and len(self.bullets) == 0:
                        self.bullets.append(self.tank_1.shot_bullet())
                        self.shot_song.play()
                    if event.key == pygame.K_DOWN and len(self.bullets) == 0:
                        self.bullets.append(self.tank_2.shot_bullet())
                        self.shot_song.play()

            if (self.score_a >= 5 or self.score_b >= 5):
                ball.x = 9999999999999
                if (self.play_end_game):
                    self.end_game_song.play()
                    self.play_end_game = False

                winner = 'P1'
                # drawing victory
                Score.center = (600, 450)
                if self.score_a > self.score_b:
                    winner = 'P2'

                victory_text = self.victory_font.render(winner+' WIN', True, WHITE, BLACK)
                screen.fill(BLACK)
                screen.blit(victory_text, self.victory_text_rect)
            else:

                keys = pygame.key.get_pressed()

                # Move p1
                self.tank_1.control(keys, [pygame.K_w, pygame.K_a, pygame.K_d], 0)
                self.tank_1.draw()
                # Move p2
                self.tank_2.control(keys, [pygame.K_UP, pygame.K_LEFT, pygame.K_RIGHT], 1)
                self.tank_2.draw()

                if collision_ball(self.tank_1.rect, ball.get_rect(), self.tank_1.ang):
                    ball.dx += math.cos(math.radians(self.tank_1.ang))
                    ball.dy -= math.sin(math.radians(self.tank_1.ang))

                if collision_ball(self.tank_2.rect, ball.get_rect(), self.tank_2.ang):
                    ball.dx += math.cos(math.radians(self.tank_2.ang))
                    ball.dy -= math.sin(math.radians(self.tank_2.ang))
                # start shot
                for b in self.bullets:
                    b.move()
                    if b.get_data()[0].x <= -50:
                        self.bullets.remove(b)
                    if ball.detection_collision(b):
                        self.bullets.remove(b)

                if ball.get_rect().colliderect(20, 277, 80, 220):
                    self.score_a += 1
                    ball.restart()
                    self.score_song.play()
                    score_1.upload_score(self.score_a)
                    self.bullets.clear()

                if ball.get_rect().colliderect((1200, 277, 80, 220)):
                    self.score_b += 1
                    ball.restart()
                    self.score_song.play()
                    score_2.upload_score(self.score_b)
                    self.bullets.clear()

            score_1.draw(screen)
            score_2.draw(screen)
            ball.move()
            pygame.display.update()
            screen.fill("#1d982b")


game = Game()
game.run()
