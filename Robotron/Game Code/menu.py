import random
import webbrowser
from playsound import playsound
import pygame

from APIinteractions import *
from constants.colors import *
from constants.const import *
from event import *
from states import *

"""
https://stackoverflow.com/questions/54363047/how-to-draw-outline-on-the-fontpygame
"""
def displaySomeText(text, y_coord, font, col, surf):
    somewords = font.render(
        text,
        True,
        col)
    width, _ = pygame.font.Font.size(font, text)
    position_font = (SCREENSIZE[0] - width) / 2
    surf.screen.blit(somewords, (position_font + 6, y_coord))

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




def render(text, font, gfcolor=pygame.Color('dodgerblue'), ocolor=(255, 130, 45), opx=4):
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

def get_ran_col():
    return random.choice(random_colors)

def randomStart(view):
    for i in range(0, SCREENSIZE[0], 2):
        for j in range(0, SCREENSIZE[1], 2):
            col = get_ran_col()
            rect = pygame.Rect((i, j), (2, 2))
            pygame.draw.rect(view.screen, col, rect)

def allopperational(view):
    view.tickcounter += 1
    if view.tickcounter == 2:
        playsound('audio/intro.mp3', block = False)
    if view.tickcounter > 40:
        view.evManager.post(ChangeState(HOMESCREEN))
    elif view.tickcounter > 5:

        view.screen.fill((10, 10, 10))

        displaySomeText('Initial tests indicate:', SCREENSIZE[1]/2-50, view.font, WHITE, view)
        displaySomeText('Operational', SCREENSIZE[1]/2+50, view.font, WHITE, view)

    else:
        randomStart(view)
    pygame.display.flip()

    view.clock.tick(TPS)


def home(view, event):

    view.screen.fill(BLACK)
    view.tickcounter += 1
    if isinstance(event, Keyboard):
        if event.key == 32:
            view.evManager.post(ChangeState(PLAYGAME))
        if event.key == 104:
            view.evManager.post(ChangeState(HELP))
        if event.key == 13:
            view.evManager.post(ChangeState(LOGIN))
        if event.key == 111:
            webbrowser.open('https://robo.johnmontgomery.tech', new=2)
    else:
        prog = list(range(40,0,-1))
        if view.tickcounter % 10 == 1:
            view.col = random.choice(title_colors)
            view.edgecol = random.choice(edge)
        for idx, letter in enumerate('ROBOTRON:'):
            image = render(letter, view.largefont, gfcolor=view.col, ocolor=view.edgecol)
            w,h = image.get_width(), image.get_height()
            image = pygame.transform.scale(image, (w, 0 if view.tickcounter<idx else h+int(1.3**prog[view.tickcounter-idx if view.tickcounter- idx<40 else 39])))
            view.screen.blit(image , (88+idx*74,90-image.get_height()/2))

        if 220 >= view.tickcounter > 40:
            view.tickcounter += 2
            image = pygame.image.load('sprites/2084.png')
            w,h = image.get_width(), image.get_height()
            image = pygame.transform.scale(image, (w, 180*h // (view.tickcounter - 40)))
            view.screen.blit(image, (196, (100+ (180*h // (view.tickcounter - 40)))/2 ))
        if 220 < view.tickcounter:
            image = pygame.image.load('sprites/2084.png')
            view.screen.blit(image, (196,140))

            displaySomeText('Created By:', 320, view.smallfont, (255,255,255), view)
            displaySomeText('John Montgomery',360, view.smallfont, (246, 130, 20), view )

            if view.tickcounter % 5 == 0:
                if view.color == (0,0,0):
                    view.color = (22, 32, 221)
                else:
                    view.color = (0,0,0)

            displaySomeText('SPACE to PLAY',400, view.font, view.color, view )
            displaySomeText("Leaderboard Available at - robotron2084.xyz", 510, view.minifont,
                            random.choice(title_colors), view)
            displaySomeText("(O to open link)", 540, view.minifont, (255, 255, 255), view)
            try:
                with open('.token', 'r')as f:
                    text = f.read().split('>')[2]
                    displaySomeText('LOGGED IN AS '+text, 470, view.smallfont, (22, 32, 221), view)

            except FileNotFoundError:
                displaySomeText("ENTER FOR LOGIN", 470, view.smallfont, (22, 32, 221), view)
            displaySomeText('ORIGINAL GAME CREATED BY: WILLIAM ELECTRONICS INC.', 570, view.minifont,(246, 130, 20), view)
    pygame.display.flip()

    view.clock.tick(TPS)

def login(view, event):
    view.screen.fill(BLACK)
    if isinstance(event, Mouse):
        if 340 < event.pos[0] < 460 and 200 < event.pos[1] < 240:
            status = loginuser(view.username, view.password)
            if status:
                view.evManager.post(ChangeState(HOMESCREEN))
            else:
                view.incorrect = 250

        elif 320 < event.pos[0] < 480 and 500 < event.pos[1] < 540:
            success = signupuser(view.username1, view.password1, view.password2, view.initials)
            if success:
                view.evManager.post(ChangeState(HOMESCREEN))
            else:
                view.incorrect = 550

        elif 0 < event.pos[0] < 50 and 0 < event.pos[1] < 50:
            view.evManager.post(ChangeState(HOMESCREEN))


    if view.incorrect:
        displaySomeText("INCORRECT", view.incorrect, view.smallfont, (200,0,0), view)

    displaySomeText('LOGIN + SIGN UP', 20, view.font, (246, 130, 20), view)
    displaySomeText('LOGIN', 205, view.smallfont, (255, 255, 255), view)

    pygame.draw.rect(view.screen, GREY, pygame.Rect(100, 100, 600, 40), width=3)

    pygame.draw.rect(view.screen, GREY, pygame.Rect(100, 150, 600, 40), width=3)

    pygame.draw.rect(view.screen, GREY, pygame.Rect(340, 200, 120, 40), width=3)

    pygame.draw.lines(view.screen, GREY, False, [(30,10),(10,25), (30, 40)], width=5)


    displaySomeText('SIGN UP', 506, view.smallfont, (255, 255, 255), view)
    pygame.draw.rect(view.screen, GREY, pygame.Rect(100, 300, 600, 40), width=3)

    pygame.draw.rect(view.screen, GREY, pygame.Rect(100, 350, 600, 40), width=3)

    pygame.draw.rect(view.screen, GREY, pygame.Rect(100, 400, 600, 40), width=3)

    pygame.draw.rect(view.screen, GREY, pygame.Rect(100, 450, 600, 40), width=3)

    pygame.draw.rect(view.screen, GREY, pygame.Rect(320, 500, 160, 40), width=3)


    if isinstance(event, Mouse):
        if 100<event.pos[0]<700 and 100<event.pos[1]<140:
            pygame.draw.rect(view.screen, WHITE, pygame.Rect(100,97,600,43), width=5)
            view.highlight = 'username'
        elif 100<event.pos[0]<700 and 150<event.pos[1]<190:
            pygame.draw.rect(view.screen, WHITE, pygame.Rect(100,147,600,43), width=5)
            view.highlight = 'password'
        elif 100<event.pos[0]<700 and 300<event.pos[1]<340:
            pygame.draw.rect(view.screen, WHITE, pygame.Rect(100, 297, 600, 43), width=5)
            view.highlight = 'username1'
        elif 100<event.pos[0]<700 and 350<event.pos[1]<390:
            pygame.draw.rect(view.screen, WHITE, pygame.Rect(100, 347, 600, 43), width=5)
            view.highlight = 'password1'
        elif 100<event.pos[0]<700 and 400<event.pos[1]<440:
            pygame.draw.rect(view.screen, WHITE, pygame.Rect(100, 397, 600, 43), width=5)
            view.highlight = 'password2'
        elif 100<event.pos[0]<700 and 450<event.pos[1]<490:
            pygame.draw.rect(view.screen, WHITE, pygame.Rect(100, 447, 600, 43), width=5)
            view.highlight = 'initials'
        else:
            view.highlight = None
    else:
        if view.highlight:
            if view.highlight == 'username':
                pygame.draw.rect(view.screen, WHITE, pygame.Rect(100, 97, 600, 43), width=5)
            elif view.highlight == 'username1':
                pygame.draw.rect(view.screen, WHITE, pygame.Rect(100, 297, 600, 43), width=5)
            elif view.highlight == 'password1':
                pygame.draw.rect(view.screen, WHITE, pygame.Rect(100, 347, 600, 43), width=5)
            elif view.highlight == 'password2':
                pygame.draw.rect(view.screen, WHITE, pygame.Rect(100, 397, 600, 43), width=5)
            elif view.highlight == 'initials':
                pygame.draw.rect(view.screen, WHITE, pygame.Rect(100, 447, 600, 43), width=5)
            else:
                pygame.draw.rect(view.screen, WHITE, pygame.Rect(100, 147, 600, 43), width=5)

    if isinstance(event, Keyboard):
        if view.highlight:
            if view.highlight == 'username':
                if event.uni != 'backspace' :
                    view.username += event.uni
                else:
                    view.username = view.username[:-1]
                if len(view.username)>40:
                    view.username = view.username[:-1]

            elif view.highlight == 'username1':
                if event.uni != 'backspace' :
                    view.username1 += event.uni
                else:
                    view.username1 = view.username1[:-1]
                if len(view.username1)>40:
                    view.username1 = view.username1[:-1]

            elif view.highlight == 'password1':
                if event.uni != 'backspace' :
                    view.password1 += event.uni
                else:
                    view.password1 = view.password1[:-1]
                if len(view.password1)>40:
                    view.password1 = view.password1[:-1]

            elif view.highlight == 'password2':
                if event.uni != 'backspace' :
                    view.password2 += event.uni
                else:
                    view.password2 = view.password2[:-1]
                if len(view.password2)>40:
                    view.password2 = view.password2[:-1]

            elif view.highlight == 'initials':
                if event.uni != 'backspace' :
                    view.initials += event.uni
                else:
                    view.initials = view.initials[:-1]
                if len(view.initials)>3:
                    view.initials = view.initials[:-1]

            else:
                if event.uni != 'backspace':
                    view.password += event.uni
                else:
                    view.password = view.password[:-1]
                if len(view.password)>40:
                    view.username = view.username[:-1]

    if view.password2 != view.password1:
        pygame.draw.rect(view.screen, RED, pygame.Rect(100, 347, 600, 43), width=5)
        pygame.draw.rect(view.screen, RED, pygame.Rect(100, 397, 600, 43), width=5)



    displaySomeText('username', 301, view.tinyfont, (255, 255, 255), view)
    displaySomeText(view.username1, 311, view.minifont, (255, 255, 255), view)
    displaySomeText('password', 351, view.tinyfont, (255, 255, 255), view)
    displaySomeText('*'*len(view.password1), 361, view.minifont, (255, 255, 255), view)
    displaySomeText('confirm password', 401, view.tinyfont, (255, 255, 255), view)
    displaySomeText('*' * len(view.password2), 411, view.minifont, (255, 255, 255), view)
    displaySomeText('initials', 451, view.tinyfont, (255, 255, 255), view)
    displaySomeText(view.initials, 461, view.tinyfont, (255, 255, 255), view)


    displaySomeText('username', 101, view.tinyfont, (255, 255, 255), view)
    displaySomeText(view.username, 111, view.minifont, (255, 255, 255), view)
    displaySomeText('password', 151, view.tinyfont, (255, 255, 255), view)
    displaySomeText('*' * len(view.password), 161, view.minifont, (255, 255, 255), view)





    pygame.display.flip()

    view.clock.tick(TPS)


def endgame(view, event):
    view.screen.fill(BLACK)
    view.tickcounter += 1
    if isinstance(event, Keyboard):
        if event.key == 32:
            view.evManager.post(ChangeState(HOMESCREEN))
        if event.key == 111:
            webbrowser.open('https://robo.johnmontgomery.tech', new=2)
        if event.key == 13:
            view.evManager.post(ChangeState(LOGIN))
    else:
        prog = list(range(40, 0, -1))
        if view.tickcounter % 10 == 1:
            view.col = random.choice(title_colors)
            view.edgecol = random.choice(edge)
        for idx, letter in enumerate('ROBOTRON:'):
            image = render(letter, view.largefont, gfcolor=view.col, ocolor=view.edgecol)
            w, h = image.get_width(), image.get_height()
            image = pygame.transform.scale(image, (w, 0 if view.tickcounter < idx else h + int(
                1.3 ** prog[view.tickcounter - idx if view.tickcounter - idx < 40 else 39])))
            view.screen.blit(image, (88 + idx * 74, 90 - image.get_height() / 2))
        if 220 >= view.tickcounter > 40:
            view.tickcounter += 2
            image = pygame.image.load('sprites/2084.png')
            w, h = image.get_width(), image.get_height()
            image = pygame.transform.scale(image, (w, 180 * h // (view.tickcounter - 40)))
            view.screen.blit(image, (196, (100 + (180 * h // (view.tickcounter - 40))) / 2))
        if 220 < view.tickcounter:
            image = pygame.image.load('sprites/2084.png')
            view.screen.blit(image, (196, 140))

            if view.tickcounter % 5 == 0:
                if view.color == (0, 0, 0):
                    view.color = (22, 32, 221)
                else:
                    view.color = (0, 0, 0)

            displaySomeText('GAME OVER', 330, view.font, view.color, view)
            displaySomeText('You Scored:', 400, view.font,  (246, 130, 20), view)
            displaySomeText(str(view.score), 450, view.font, (246, 130, 20), view)
            displaySomeText('SPACE for homescreen', 450, view.smallfont, (246, 130, 20), view)
            displaySomeText('O to open leaderboard', 525, view.smallfont, (246, 130, 20), view)


            if checkonline():
                if isloggedin():
                    if addscore(view.score):
                        displaySomeText('Score added to leaderboard', 550, view.smallfont, (246, 130, 20), view)

                else:
                    displaySomeText('Enter to log in', 550, view.smallfont, (246, 130, 20), view)
            else:
                displaySomeText('OFFLINE', 550, view.smallfont, RED, view)

    pygame.display.flip()

    view.clock.tick(TPS)