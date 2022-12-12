import turtle


def make_triangles(x, y):
    # it is used to draw out the pen
    tess.penup()

    # it is used to move cursor at x
    # and y position
    tess.goto(x, y)

    # it is used to draw in the pen
    tess.pendown()
    for i in range(3):
        # move cursor 100 unit
        # digit forward
        tess.forward(100)

        # turn cursor 120 degree left
        tess.left(120)

        # Again,move cursor 100 unit
        # digit forward
        tess.forward(100)


# Screen() method to get screen
mainScreen = turtle.Screen()

# creating tess object
tess = turtle.Turtle()

# special built in function to send current
# position of cursor to triangle
turtle.onscreenclick(make_triangles, 1)

turtle.listen()

# hold the screen
turtle.done()
