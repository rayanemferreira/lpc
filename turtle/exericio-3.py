import turtle


def make_triangles(x, y):
  
    tess.penup()

   
    tess.goto(x, y)

   
    tess.pendown()
    for i in range(3):
       
        tess.forward(100)

        
        tess.left(120)

       
        tess.forward(100)



mainScreen = turtle.Screen()


tess = turtle.Turtle()


turtle.onscreenclick(make_triangles, 1)

turtle.listen()


turtle.done()
