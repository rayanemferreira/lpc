from pygame import sprite, image, transform
from characters_module import sprites
from constants.const import *
from characters_module.sprites import stretech_image

class Character(sprite.Sprite):
    """
    This is a very basic character, from which all the other characters will extend, this is never used directly,
    and there will need to be lots of extra functions. This code mostly is needed for the animation and directions
    """
    def __init__(self, sheetname, imagecount=12, scale=30):
        """
        This creates the character, mostly handles grabing the spritesheet, clipping the sprites and scaling them.
        """
        super().__init__()
        self.sheetname = sheetname
        self.spritesheet = image.load(self.sheetname).convert()
        h,w = self.spritesheet.get_height(), self.spritesheet.get_width()/imagecount
        self.images = [transform.scale(sprite_item, (scale,scale)) for sprite_item in
                       sprites.loadStrip((0, 0, w, h), imagecount, self.spritesheet)]

        self.direction = 'N'
        self.position  = (300,200)
        self.moving = (0,0)
        self.image = self.images[0]
        self.rect = (300,200)

    def setdir(self, mov, dir):
        """
        This sets the current direction (for the spirte animation) based on the where the character is moving and facing
        """
        if dir:
            if mov > 0:
                self.direction = 'E'
            if mov < 0:
                self.direction = 'W'
        else:
            if mov > 0:
                self.direction = 'S'
            if mov < 0:
                self.direction = 'N'


    def onstart(self, view):
        """
        When the character is created, this places it onto the screen, adding some stretch
        """
        view.screen.fill((0, 0, 0))
        img, h = stretech_image(self.images[0], 30-view.tickcounter)
        posx, posy = self.position
        view.screen.blit(img, (posx, posy - h / 2))