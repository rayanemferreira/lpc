"""
These constants control game play. Most of these constants are adjustable and will adapt automatically for the game.
"""

from math import sqrt

VELOCITY = 6
DVELOCITY = sqrt(2*(VELOCITY**2))
SCREENSIZE = (800,600)
TPS = 28
TITLE = 'Robotron 2084'
PROJ_VELOCITY = 8
DPROJ_VELOCITY = sqrt(2*(PROJ_VELOCITY**2))
COOLDOWN = 5
BORDER_W = 10
BORDERSPEED = 15
