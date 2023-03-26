from characters_module.characters import Character
from constants.const import *


class Player(Character):
    """
    Because most of the logic about whether a player is alive and the score is handled by the Model, most of it
    can be abstracted away. This class mostly handles the player screen logic, and doesnt look ay the logic of whether
    or not the player is alive.
    """
    def __init__(self):
        self.sheetname = 'sprites/player.png'
        Character.__init__(self, self.sheetname)
        self.l_images = self.images[:3]
        self.r_images = self.images[3:6]
        self.f_images = self.images[6:9]
        self.u_images = self.images[9:12]

    def getskin(self, count):
        if self.direction[0] == 'N':
            return self.u_images[count]
        elif self.direction[0] == 'S':
            return self.f_images[count]
        elif self.direction[0] == 'W':
            return self.l_images[count]
        elif self.direction[0] == 'E':
            return self.r_images[count]

    def movy(self, newMov):
        if (25+BORDER_W < self.position[1] + newMov < SCREENSIZE[1]-BORDER_W*2-30) :
            self.position = (self.position[0], self.position[1] + newMov)
        self.setdir(newMov, 0)

    def movx(self, newMov):
        if (BORDER_W-10 < self.position[0] + newMov < SCREENSIZE[0]-BORDER_W*2 -10):
            self.position =  (self.position[0]+newMov,self.position[1])
        self.setdir(newMov, 1)