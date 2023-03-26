import pygame

import menu
import testing
from characters_module.player import Player
from constants.const import *
from decorations.border import Border
from event import *
from states import *
import gameplay
from characters_module.humans import *
from characters_module.enemy import *

class GraphicalView(object):
    """
    Draws the model state onto the screen.
    """

    def __init__(self, evManager, model):
        """
        evManager (EventManager): Allows posting messages to the event queue.
        model (GameEngine): a strong reference to the game Model.

        Attributes:
        isinitialized (bool): pygame is ready to draw.
        screen (pygame.Surface): the screen surface.
        clock (pygame.time.Clock): keeps the fps constant.
        smallfont (pygame.Font): a small font.
        """

        self.evManager = evManager
        self.model = model
        evManager.add_listener(self)
        self.isinitialized = False
        self.screen = None
        self.clock = None
        self.minifont = None
        self.smallfont = None
        self.font = None
        self.largefont = None
        self.skincount = 0
        self.player = None
        self.currentDown = {
            97: 0,
            100: 0,
            115: 0,
            119: 0
        }
        self.spriteslist = pygame.sprite.Group()
        self.border = Border()
        self.spriteslist.add(self.border)
        self.lastshot = 0
        self.tickcounter = 0
        self.titlecolor = (0,0,0)
        self.color = (0,0,0)
        self.username = ''
        self.password = ''
        self.highlight = None
        self.username1 = ''
        self.password1 = ''
        self.password2 = ''
        self.initials = ''
        self.incorrect = False
        self.level = 1
        self.lives = 3
        self.score = 0
        self.leveldata = {}

    def notify(self, event_in):
        """
        Receive events posted to the message queue.
        """
        if isinstance(event_in, Start):
            self.initialize()
        elif isinstance(event_in, ChangeState):
            self.tickcounter = 0
        elif isinstance(event_in, EndGame):
            # shut down the pygame graphics
            self.isinitialized = False
            pygame.quit()
        elif isinstance(event_in, Tick) or isinstance(event_in, Keyboard) or isinstance(event_in, KeyboardUp)  or isinstance(event_in, Mouse):
            currentstate = self.model.statem.peek()
            if currentstate == STATE_TEST:
                testing.testing(event_in, self)
            if currentstate == STATE_INTRO1:
                menu.allopperational(self)
            if currentstate == HOMESCREEN:
                menu.home(self, event_in)
            if currentstate == LOGIN:
                menu.login(self, event_in)
            if currentstate == PLAYGAME:
                self.evManager.post(ChangeState(LOAD_LEVEL1))
            if currentstate == ENDGAME:
                menu.endgame(self, event_in)
            if currentstate>200:
                gameplay.loadlevel(self, currentstate-200)
            if 99<currentstate<200:
                gameplay.level(self, event_in)


    def clearScreen(self):
        self.screen.fill((0, 0, 0))

    def initialize(self):
        """
        Set up the pygame graphical display and loads graphical resources.
        """

        result = pygame.init()
        pygame.font.init()
        pygame.display.set_caption(TITLE)
        self.screen = pygame.display.set_mode(SCREENSIZE)
        self.clock = pygame.time.Clock()
        self.tinyfont = pygame.font.Font('font/robotron-2084.ttf', 10)
        self.minifont = pygame.font.Font('font/robotron-2084.ttf', 18)
        self.smallfont = pygame.font.Font('font/robotron-2084.ttf', 28)
        self.font = pygame.font.Font('font/robotron-2084.ttf', 34)
        self.largefont = pygame.font.Font('font/robotron-2084.ttf', 80)
        self.isinitialized = True
        self.player = Player()
        self.lives = 3
