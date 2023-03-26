
import pygame

from constants.colors import *
from constants.const import *
from event import *
from objects.bullet import Bullet

_circle_cache = {}
def _circlepoints(r):
    r = int(round(r))
    if r in _circle_cache:
        return _circle_cache[r]
    x, y, e = r, 0, 1 - r
    _circle_cache[r] = points = []
    while x >= y:
        points.append((x, y))
        y += 1
        if e < 0:
            e += 2 * y - 1
        else:
            x -= 1
            e += 2 * (y - x) - 1
    points += [(y, x) for x, y in points if x > y]
    points += [(-x, y) for x, y in points if x]
    points += [(x, -y) for x, y in points if y]
    points.sort()
    return points

def render(text, font, gfcolor=pygame.Color('dodgerblue'), ocolor=(255, 255, 255), opx=2):
    textsurface = font.render(text, True, gfcolor).convert_alpha()
    w = textsurface.get_width() + 2 * opx
    h = font.get_height()

    osurf = pygame.Surface((w, h + 2 * opx)).convert_alpha()
    osurf.fill((0, 0, 0, 0))

    surf = osurf.copy()

    osurf.blit(font.render(text, True, ocolor).convert_alpha(), (0, 0))

    for dx, dy in _circlepoints(opx):
        surf.blit(osurf, (dx + opx, dy + opx))

    surf.blit(textsurface, (opx, opx))
    return surf

def testing(event, view):
    player = view.player

    if not view.isinitialized:
        return
    view.screen.fill(BLACK)

    if view.tickcounter <= 30:
        view.player.onstart(view)

    view.tickcounter += 1
    if isinstance(event, Keyboard):
        view.currentDown[event.key] = 1

    if isinstance(event, KeyboardUp):
        view.currentDown[event.key] = 0

    shoot = ''
    v = VELOCITY if sum(view.currentDown.values()) > 1 else DVELOCITY
    for key in view.currentDown.keys():
        if view.currentDown[key]:
            if key == 119:
                player.movy(-v)
            if key == 115:
                player.movy(v)
            if key == 97:
                player.movx(-v)
            if key == 100:
                player.movx(v)
            if len(shoot) < 2:
                if key == 105:
                    shoot += 'N'
                if key == 107:
                    shoot += 'S'
                if key == 106:
                    shoot += 'W'
                if key == 108:
                    shoot += 'E'

    if shoot:
        if view.lastshot == 0:
            bullet = Bullet(player.position[0], player.position[1], shoot)
            view.spriteslist.add(bullet)
            view.lastshot += COOLDOWN
        else:
            view.lastshot -= 1

    view.spriteslist.update()
    game_surface = pygame.Surface(SCREENSIZE, pygame.SRCALPHA, 32)
    game_surface = game_surface.convert_alpha()
    view.spriteslist.draw(game_surface)

    view.skincount += 1 if view.tickcounter%2 == 0 else 0
    if view.skincount > 2:
        view.skincount = 0

    # clear display
    # draw some words on the screen

    somewords = view.smallfont.render(
        'This is a testing screen',
        True,
        (0, 255, 0))
    width, _ = pygame.font.Font.size(view.smallfont, 'This is a testing screen')
    position_font = (SCREENSIZE[0] - width) / 2
    view.screen.blit(somewords, (position_font+6, 0))



    view.screen.blit(game_surface, (0, 0))
    if view.tickcounter > 30:
        view.screen.blit(player.getskin(view.skincount), player.position)
    view.clock.tick(TPS)
    # flip the display to show whatever we drew

    pygame.display.flip()

