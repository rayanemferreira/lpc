import pygame

pygame.font.init()


class Score:
    def __init__(self, score_a, weight, color):
        self.scoreA = score_a
        self.color = color
        self.font = pygame.font.Font("sprites/PressStart2P.ttf", 40)
        self.score_point_player = self.font.render(f"{self.scoreA}", True, color)
        self.score_point_player_rect = self.score_point_player.get_rect(center=(weight, 25))

    def draw(self, screen):
        screen.blit(self.score_point_player, self.score_point_player_rect)

    def upload_score(self, score):
        self.scoreA = score
        self.score_point_player = self.font.render(f"{self.scoreA}", True, self.color)
