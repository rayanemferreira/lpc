
from characters_module.characters import Character
from constants.const import *
import random
import pygame
class Enemy(Character):
    """
    This enemy is again, only used to extend from. It acts as a basic super class which can easily be used to generate
    the other classes for the enemies. Because the enemies need to update in different ways, its not possible to have
    them all exhibit the same behaviour here.
    """
    def __init__(self,sheetname, images=12):
        Character.__init__(self, sheetname, images)
        self.rect = (random.randint(50,SCREENSIZE[0]-50),random.randint(70,SCREENSIZE[1]-50) )



class Grunt(Enemy):
    """
    This is the basic enemy, which is only able to move, and on colliding with the player, it kills the player. If it
    gets hit by a bullet, it dies
    """
    def __init__(self):
        self.sheetname = 'sprites/grunt.png'
        Enemy.__init__(self, self.sheetname)
        self.vx = random.randint(-20,20)

        self.vy = random.randint(-20, 20)
    def update(self, count, movx,movy):
        """
        This is a pretty poorly executed AI. I think ill replace this with a boids algorithm.
        """

        self.image = self.images[count]
        position = self.rect
        x = movx
        y = movy
        legnth = sqrt(x**2 + y**2)
        adj = legnth / 3
        newy = y / adj
        newx = x / adj

        newx = max(50,min(self.rect[0]+newx, SCREENSIZE[0]-50))
        newy = max(50, min(self.rect[1]+newy, SCREENSIZE[1]-50))

        self.rect = (newx, newy)

class Electrode(Enemy):
    """
    These are the static enemies
    """
    def __init__(self):
        self.sheetname = 'sprites/electrode.png'
        Enemy.__init__(self, self.sheetname,3)
        self.image = random.choice(self.images)
        self.image = pygame.transform.scale(self.image, (20,20))
    def update(self, count, _):
        return


class Hulk(Enemy):
    """
    These are like the grunts, but cant be killed. They only slow down when hit.
    """
    def __init__(self):
        self.sheetname = 'sprites/hulk.png'
        Enemy.__init__(self, self.sheetname)
        self.living = 0

    def getskin(self, count):
        """
        This is overriding the base function. Hulks always face the same way
        """
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

    def update(self, count, _):
        if not self.living % 25:
            self.velocity = (random.choice((-3, 3, 0)), random.choice((-3, 3, 0)))
        flag = False
        while not flag:
            if (35 + BORDER_W < self.rect[1] + self.velocity[1] < SCREENSIZE[1] - BORDER_W * 2 - 35):
                self.rect = (self.rect[0], self.rect[1] + self.velocity[1])
                flag = True
            else:
                self.velocity = (random.choice((-4, 4, 0)), random.choice((-4, 4, 0)))
            if (BORDER_W - 20 < self.rect[0] + self.velocity[0] < SCREENSIZE[0] - BORDER_W * 2 - 20):
                self.rect = (self.rect[0] + self.velocity[0], self.rect[1])
            else:
                self.velocity = (random.choice((-4, 4, 0)), random.choice((-4, 4, 0)))

        self.living += 1

        self.image = self.getskin(count)

    def kill(self):
        self.velocity = (random.choice((-2, 2, 0)), random.choice((-2, 2, 0)))
        flag = False
        while not flag:
            if (35 + BORDER_W < self.rect[1] + self.velocity[1] < SCREENSIZE[1] - BORDER_W * 2 - 35):
                self.rect = (self.rect[0], self.rect[1] + self.velocity[1])
                flag = True
            else:
                self.velocity = (random.choice((-3, 3, 0)), random.choice((-3, 3, 0)))
            if (BORDER_W - 20 < self.rect[0] + self.velocity[0] < SCREENSIZE[0] - BORDER_W * 2 - 20):
                self.rect = (self.rect[0] + self.velocity[0], self.rect[1])
            else:
                self.velocity = (random.choice((-3, 3, 0)), random.choice((-3, 3, 0)))

class Brain(Enemy):
    def __init__(self):
        self.sheetname = 'sprites/brain.png'
        Enemy.__init__(self, self.sheetname)


class Spheroids(Enemy):
    def __init__(self):
        self.sheetname = 'sprites/spheroids.png'
        Enemy.__init__(self, self.sheetname, 8)


class Quarks(Enemy):
    def __init__(self):
        self.sheetname = 'sprites/quark.png'
        Enemy.__init__(self, self.sheetname, 8)


class Enforcer(Enemy):
    def __init__(self):
        self.sheetname = 'sprites/enforcer.png'
        Enemy.__init__(self, self.sheetname, 6)
        self.image = self.images[1]

class Tank(Enemy):
    def __init__(self):
        self.sheetname = 'sprites/tank.png'
        Enemy.__init__(self, self.sheetname, 4)