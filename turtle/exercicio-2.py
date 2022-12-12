from turtle import *

speed('fastest')


right(-90)


angle = 30


def choosing_pain(level):
    pencolor(0, 255 // level, 0)


def direct(level, sz):
    choosing_pain(level)

    rt(angle)
    fd(-sz)


def setting_nc(level, sz):
  
    choosing_pain(level)

    
    fd(sz)

    rt(angle)



def trace_branches(sz, level):
    if level > 0:
        colormode(255)
        setting_nc(level, sz)

       
        trace_branches(0.8 * sz, level - 1)

        choosing_pain(level)

        lt(2 * angle)

       
        trace_branches(0.8 * sz, level - 1)

        direct(level, sz)



trace_branches(80, 7)
