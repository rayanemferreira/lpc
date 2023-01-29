import pygame


def create_arena():
    wall_list = []

    # Parse the level string above. W = wall, E = exit
    x = y = 0
    for row in level:
        for col in row:
            if col == "W":
                wall_list.append(pygame.Rect(x, y, 40, 40))
            x += 40
        y += 40
        x = 0

    return wall_list


# Holds the level layout in a list of strings.
level = [
    "                    ",
    "WWWWWWWWWWWWWWWWWWWW",
    "W        WW        W",
    "W        WW        W",
    "W                  W",
    "W   WW        WW   W",
    "W                  W",
    "W                  W",
    "W        WW        W",
    "W                  W",
    "W                  W",
    "W   WW        WW   W",
    "W        WW        W",
    "W        WW        W",
    "WWWWWWWWWWWWWWWWWWWW",
]
