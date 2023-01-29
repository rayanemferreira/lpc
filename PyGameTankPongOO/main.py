import pygame
from tank import Tank
import arena
import collision
# from bulletclass import Bullet


class Game(object):
    def __init__(self, width=800, height=600):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Combat")

        self.clock = pygame.time.Clock()

        self.game_over = False

        self.player_1 = Tank(70, 340, '1')
        self.bullets_1 = self.player_1.get_player_bullets()
        self.player_2 = Tank(730, 340, '2')
        self.bullets_2 = self.player_2.get_player_bullets()

        self.wall_list = arena.create_arena()

        self.game_loop = True

    def run(self):

        while self.game_loop:
            self.clock.tick(60)
            if not self.game_over:
                for b in self.bullets_1:
                    b.move()
                for b in self.bullets_2:
                    b.move()

                keys = pygame.key.get_pressed()
                if keys[pygame.K_a]:
                    self.player_1.turn_left()
                if keys[pygame.K_d]:
                    self.player_1.turn_right()
                if keys[pygame.K_w]:
                    self.player_1.move()

                if keys[pygame.K_LEFT]:
                    self.player_2.turn_left()
                if keys[pygame.K_RIGHT]:
                    self.player_2.turn_right()
                if keys[pygame.K_UP]:
                    self.player_2.move()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_loop = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        if not self.game_over:
                            self.player_1.shoot()
                    if event.key == pygame.K_DOWN:
                        if not self.game_over:
                            self.player_2.shoot()

            collision.tank_collision(self.player_1, self.player_2)
            collision.tank_collision(self.player_2, self.player_1)
            for wall in self.wall_list:
                collision.wall_collision(self.player_1, wall)
                collision.wall_collision(self.player_2, wall)

            # update self.screen
            self.screen.fill(((151, 163, 67, 255)))
            self.player_1.draw(self.screen)
            self.player_2.draw(self.screen)
            for b in self.bullets_1:
                b.draw(self.screen)
            for b in self.bullets_2:
                b.draw(self.screen)
            for wall in self.wall_list:
                pygame.draw.rect(self.screen, (253, 181, 104, 255), wall)
            pygame.display.update()


game = Game(800, 600)
game.run()
