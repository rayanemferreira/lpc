import pygame
from robots import Robots

def get_zona():

    list_aux = [pygame.Rect(20, 157, 180, 10), pygame.Rect(20, 617, 180, 10), pygame.Rect(200, 167, 10, 440),
                pygame.Rect(1100, 157, 180, 10), pygame.Rect(1100, 617, 180, 10), pygame.Rect(1090, 167, 10, 440)]
    return list_aux

class Arena:
    def __init__(self, num_arena, screen):
        self.num_arena = num_arena
        self.screen = screen
        self.taxa = 0.05
        self.robot_1 = Robots(650, 400, 30, 60, self.screen, (255, 255, 255))
        self.robot_2 = Robots(75, 900, 30, 60, self.screen, (255, 255, 255))

    def draw_object(self):
        # draw L left
        list_reacts = []
        list_aux = []
        # draw screen
        pygame.draw.line(self.screen, (255, 255, 255), (650, 75), (650, 725), 5)
        camp_player_1 = pygame.draw.rect(self.screen, (255, 255, 255), (20, 277, 80, 220), 5)
        camp_player_2 = pygame.draw.rect(self.screen, (255, 255, 255), (1200, 277, 80, 220), 5)

        list_reacts.append(camp_player_1)
        list_reacts.append(camp_player_2)

        # player´s zone
        pygame.draw.rect(self.screen, "#ffffff", (20, 167, 180, 440), 5)
        pygame.draw.rect(self.screen, "#ffffff", (1100, 167, 180, 440), 5)

        screen_1 = pygame.draw.rect(self.screen, "#ffffff", (0, 50, 1300, 25))
        list_reacts.append(screen_1)
        list_aux.append(screen_1)

        screen_2 = pygame.draw.rect(self.screen, "#ffffff", (0, 725, 1300, 25))
        list_reacts.append(screen_2)
        list_aux.append(screen_2)

        screen_3 = pygame.draw.rect(self.screen, "#ffffff", (1275, 75, 25, 650))
        list_reacts.append(screen_3)

        screen_6 = pygame.draw.rect(self.screen, "#ffffff", (0, 75, 25, 650))
        list_reacts.append(screen_6)

        while True:
            self.robot_2.move()
            self.robot_1.move()

            list_reacts.append(self.robot_1.get_rect())
            list_reacts.append(self.robot_2.get_rect())

            return list_reacts
