import pygame.mixer

from tank import Tank
from config import *
from score import Score
from ball import Ball
pygame.init()


class Game:
    pygame.mixer.init()

    def __init__(self):
        self.game_loop = True
        self.clock = pygame.time.Clock()

        self.player1_rect = pygame.Rect(125, 363, 80, 80)
        self.player2_rect = pygame.Rect(1120, 363, 80, 80)
        self.score_a = self.score_b = 0
        self.bullets = []
        self.tank_1 = Tank(0, 90, self.player1_rect, "sprites/nave-1.png", RED)
        self.tank_2 = Tank(180, -90, self.player2_rect, "sprites/nave-2.png", BLUE)

    def run(self):
        self.clock.tick(80)

        score_1 = Score(self.score_a, 300, RED)
        score_2 = Score(self.score_b, 980, BLUE)
        ball = Ball(625, 363, 50, 50)
        while self.game_loop:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_loop = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.game_loop = False
                    if event.key == pygame.K_q and len(self.bullets) == 0:
                        self.bullets.append(self.tank_1.shot_bullet())
                    if event.key == pygame.K_SEMICOLON and len(self.bullets) == 0:
                        self.bullets.append(self.tank_2.shot_bullet())
            keys = pygame.key.get_pressed()

            # Move p1
            self.tank_1.control(keys, [pygame.K_w, pygame.K_a, pygame.K_d], 0)
            self.tank_1.draw()
            # Move p2
            self.tank_2.control(keys, [pygame.K_UP, pygame.K_LEFT, pygame.K_RIGHT], 1)
            self.tank_2.draw()

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
                score_1.upload_score(self.score_a)
                self.bullets.clear()

            if ball.get_rect().colliderect((1200, 277, 80, 220)):
                self.score_b += 1
                ball.restart()
                score_2.upload_score(self.score_b)
                self.bullets.clear()

            score_1.draw(screen)
            score_2.draw(screen)
            ball.move()
            pygame.display.update()
            screen.fill("#748f00")


game = Game()
game.run()
