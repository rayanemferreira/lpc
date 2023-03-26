import pygame


class Arena:
    def __init__(self, num_arena, screen):
        self.num_arena = num_arena
        self.screen = screen

    def draw_object(self):
        # draw L left
        list_reacts = []

        # draw screen

        pygame.draw.line(self.screen, (255, 255, 255), (650, 75), (650, 725), 5)
        pygame.draw.circle(self.screen, (255, 255, 255), (25, 387), 110, 5)
        pygame.draw.circle(self.screen, (255, 255, 255), (1275, 387), 110, 5)

        screen_1 = pygame.draw.rect(self.screen, "#c29f2e", (0, 50, 1300, 25))
        list_reacts.append(screen_1)

        screen_2 = pygame.draw.rect(self.screen, "#c29f2e", (0, 725, 1300, 25))
        list_reacts.append(screen_2)

        screen_3 = pygame.draw.rect(self.screen, "#c29f2e", (1275, 75, 25, 650))
        list_reacts.append(screen_3)

        screen_6 = pygame.draw.rect(self.screen, "#c29f2e", (0, 75, 25, 650))
        list_reacts.append(screen_6)

        screen_7 = pygame.draw.rect(self.screen, "#c29f2e", (350, 260, 25, 60))
        list_reacts.append(screen_7)

        screen_8 = pygame.draw.rect(self.screen, "#c29f2e", (350, 500, 25, 60))
        list_reacts.append(screen_8)

        screen_9 = pygame.draw.rect(self.screen, "#c29f2e", (950, 260, 25, 60))
        list_reacts.append(screen_9)

        screen_10 = pygame.draw.rect(self.screen, "#c29f2e", (950, 500, 25, 60))
        list_reacts.append(screen_10)

        return list_reacts
