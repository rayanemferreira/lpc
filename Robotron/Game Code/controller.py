
import pygame

from event import *


class Controller:
    def __init__(self, eventManager, model):
        self.eventManager = eventManager
        eventManager.add_listener(self)
        self.model = model

    def notify(self, event):
        if isinstance(event, Tick):

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self.eventManager.post(EndGame())
                if event.type == pygame.KEYDOWN:
                    if event.key != pygame.K_ESCAPE:
                        if event.key != pygame.K_BACKSPACE:
                            self.eventManager.post(Keyboard(event.key,event.unicode))
                        else:
                            self.eventManager.post(Keyboard(event.key, 'backspace'))
                    else:
                        self.eventManager.post(EndGame())
                if event.type == pygame.KEYUP:
                    self.eventManager.post(KeyboardUp(event.key))

                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.eventManager.post(Mouse(event.pos))