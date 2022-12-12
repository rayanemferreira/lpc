from turtle import *

speed('fastest')

# turning the turtle to face upwards
right(-90)

# the acute angle between
# the base and branch of the Y
angle = 30


def choosing_pain(level):
    pencolor(0, 255 // level, 0)


def direct(level, sz):
    choosing_pain(level)

    rt(angle)
    fd(-sz)


def setting_nc(level, sz):
    # splitting the rgb range for green color
    # into equal intervals for each level
    # setting the colour according
    # to the current level
    choosing_pain(level)

    # drawing the base
    fd(sz)

    rt(angle)


# function to plot a Y
def trace_branches(sz, level):
    if level > 0:
        colormode(255)
        setting_nc(level, sz)

        # recursive call for
        # the right subtree
        trace_branches(0.8 * sz, level - 1)

        choosing_pain(level)

        lt(2 * angle)

        # recursive call for
        # the left subtree
        trace_branches(0.8 * sz, level - 1)

        direct(level, sz)


# tree of size 80 and level 7
trace_branches(80, 7)
