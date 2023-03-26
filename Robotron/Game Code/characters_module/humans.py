from characters_module.characters import Character
import random
from constants.const import *
import time
class Human(Character):
    """
    The base Human class.  Because the behaviour is so similar here (they all have the same movement and actions) so
    they can all extend from a very very basic class.
    """
    def __init__(self,sheetname, images=12):
        Character.__init__(self, sheetname, images, 60)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(50, SCREENSIZE[0] - 50), random.randint(70, SCREENSIZE[1] - 50))


    def update(self,count, _):
        if not self.living % 25 :
            self.velocity = (random.choice((-4, 4,0)), random.choice((-4, 4,0)))
        flag = False
        while not flag:
            if (35+BORDER_W < self.rect[1] + self.velocity[1] < SCREENSIZE[1]-BORDER_W*2-35):
                self.rect = (self.rect[0], self.rect[1]+self.velocity[1])
                flag = True
            else:
                self.velocity = (random.choice((-4, 4, 0)), random.choice((-4, 4, 0)))
            if (BORDER_W-20 < self.rect[0] + self.velocity[0] < SCREENSIZE[0]-BORDER_W*2 -20):
                self.rect = (self.rect[0]+self.velocity[0], self.rect[1])
            else:
                self.velocity = (random.choice((-4, 4, 0)), random.choice((-4, 4, 0)))

        self.living += 1

        self.image = self.getskin(count)

    def die(self, view):
        value = self.value
        somewords = view.minifont.render(
            self.value,
            True,
            (246, 130, 20))
        view.screen.blit(somewords, self.rect)
        time.sleep(0.05)
        self.kill()
        return int(value)

    def getskin(self, count):
        if self.velocity[0] < 0:
            return self.images[:3][count]
        elif self.velocity[0] > 0:
            return self.images[3:6][count]
        elif self.velocity[1] < 0:
            return self.images[6:9][count]
        elif self.velocity[1] > 0:
            return self.images[9:12][count]
        else:
            return self.images[0]



class Mommies(Human):
    def __init__(self):
        self.sheetname = 'sprites/mommies.png'
        self.living = 0
        self.velocity = (random.randint(-4, 4), random.randint(-4, 4))
        self.value = '1000'
        Character.__init__(self, self.sheetname)




class Daddies(Human):
    def __init__(self):
        self.sheetname = 'sprites/daddies.png'
        self.living = 0
        self.velocity = (random.randint(-4, 4), random.randint(-4, 4))
        self.value = '1000'
        Character.__init__(self, self.sheetname)



class Mikeys(Human):
    """
    These are the 'kids' - i made them move slower
    """
    def __init__(self):
        self.sheetname = 'sprites/mikeys.png'
        self.living = 0
        self.velocity = (random.randint(-3, 3), random.randint(-3, 3))
        self.value = '1000'
        Character.__init__(self, self.sheetname)

