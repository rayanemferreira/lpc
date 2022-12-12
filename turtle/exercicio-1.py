import turtle
import math


def Get_Next_Fibonacci_Number(square_a, square_b):
    temp = square_b
    square_b = square_b + square_a
    square_a = temp
    return square_a, square_b


def Draw_A_Square(square_b, x_factor, loops):
    for j in range(loops):
        x.forward(square_b * x_factor)
        x.left(90)
    x.forward(square_b * x_factor)


def Bringing_The_Pen():
    x.penup()
    x.setposition(factor, 0)
    x.seth(0)
    x.pendown()


def fiboPlot(N):
    a = 0
    b = 1

    square_a, square_b = Get_Next_Fibonacci_Number(a, b)

    x.pencolor("blue")

    
    Draw_A_Square(square_b, factor, 3)
    
    square_a, square_b = Get_Next_Fibonacci_Number(square_a, square_b)

    # Drawing the rest of the squares
    for i in range(1, N):
        x.backward(square_a * factor)
        x.right(90)

        Draw_A_Square(square_b, factor, 2)

        square_a, square_b = Get_Next_Fibonacci_Number(square_a, square_b)

   
    Bringing_The_Pen()

   
    x.pencolor("red")

  
    x.left(90)
    for i in range(N):
        print(b)
        fdw = math.pi * b * factor / 2
        fdw /= 90
        for j in range(90):
            x.forward(fdw)
            x.left(1)
        a, b = Get_Next_Fibonacci_Number(a, b)


factor = 1

n = int(input('Enter the number of iterations (must be > 1): '))


if n > 0:
    print("Fibonacci series for", n, "elements :")
    x = turtle.Turtle()
    x.speed(100)
    fiboPlot(n)
    turtle.done()
else:
    print("Number of iterations must be > 0")
