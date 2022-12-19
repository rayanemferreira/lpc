import turtle
import time
import random
from playsound import playsound

# Draw screen
screen = turtle.Screen()
screen.title("Breakout")
screen.bgcolor("black")
screen.setup(width=450, height=650)
screen.tracer(0)

# Draw paddle
paddle = turtle.Turtle()
paddle.speed(0)
paddle.shape("square")
paddle.color("blue")
paddle.shapesize(stretch_wid=0.5, stretch_len=2)
paddle.penup()
paddle.goto(0, -250)

# Draw ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.shapesize(stretch_wid=0.3, stretch_len=0.3)
ball.penup()
ball.goto(0, 0)
ball.dx = random.choice((8, 9, 10, 11))
ball.dy = random.choice((-8, -9, -10, -11))

# Draw block
x_list = [188, 159.1, 130.2, 101.3, 72.4, 43.5, 14.5,
          -14.5, -43.5, -72.4, -101.3, -130.2, -159.1, -188]
y_list = [190, 180, 170, 160, 150, 140, 130, 120]
block_list = []

index = 0

for i in y_list:
    for j in x_list:
        block = turtle.Turtle()
        block.shape('square')
        block.shapesize(stretch_len=1.2, stretch_wid=0.3)

        if (index < 2):
            block.color('red')
        elif (index >= 2 and index < 4):
            block.color('orange')
        elif (index >= 4 and index < 6):
            block.color('green')
        else:
            block.color('yellow')

        block.up()
        block.goto(j, i)
        block_list.append(block)

    index += 1

block_count = len(block_list)

# Score
score = 0
highest_score = 0
life = 4


# Head-up display
def draw_hud(widht, height, value):
    hud = turtle.Turtle()
    hud.speed(0)
    hud.shape("square")
    hud.color("white")
    hud.penup()
    hud.hideturtle()
    hud.goto(widht, height)
    hud.write(f"{value}", align="center",
              font=("Press Start 2P", 24, "normal"))
    return hud


hud_score = draw_hud(-130, 200, 0)
hud_highest = draw_hud(130, 200, 0)
hud_life = draw_hud(72, 250, 4)


# Screen limit
def screen_limit(stretch_wid, stretch_len, width, height):
    limit = turtle.Turtle()
    limit.speed(0)
    limit.shape("square")
    limit.color("white")
    limit.shapesize(stretch_wid, stretch_len)
    limit.penup()
    limit.goto(width, height)
    return limit


screen_limit(30, 0.3, 200, 0)  # Right
screen_limit(30, 0.3, -200, 0)  # Left
screen_limit(1, 20.3, 0, 300)  # Top


# Paddle movement
def paddle_left():
    x = paddle.xcor()
    if x > -175:
        x += -20
    else:
        x = -175
    paddle.setx(x)


def paddle_right():
    x = paddle.xcor()
    if x < 175:
        x += 20
    else:
        x = 175
    paddle.setx(x)


# Collision with the wall
def collision_wall():
    if ball.ycor() > 280:
        playsound("bounce.wav")
        ball.dy *= -1
    if ball.xcor() > 190 or ball.xcor() < -190:
        playsound("bounce.wav")
        ball.dx *= -1


# Collision with the paddle
def collision_paddle():
    if -240 >= ball.ycor() > -250 and\
       paddle.xcor() + 24 > ball.xcor() > paddle.xcor() - 24:
        ball.sety(-240)
        ball.dy *= -1
        playsound("bounce.wav")


# keyboard
screen.listen()
screen.onkeypress(paddle_left, "Left")
screen.onkeypress(paddle_right, "Right")

while block_count:
    screen.update()
    time.sleep(0.05)

    # Ball movement
    ball.goto(ball.xcor() + ball.dx, ball.ycor() + ball.dy)

    # Collisions
    collision_wall()
    collision_paddle()

    # collision with lower wall
    if ball.ycor() < -290:
        score += 1
        life -= 1
        hud_score.clear()
        hud_score.write(f"{score}", align="center",
                        font=("Press Start 2P", 24, "normal"))
        hud_life.clear()
        hud_life.write(f"{life}", align="center",
                       font=("Press Start 2P", 24, "normal"))
        playsound("bounce.wav")
        ball.goto(0, 0)
        ball.dy *= -1

    # Colission with block
    if ball.ycor() < -280:
        ball.goto(0, 0)
        ball.dx *= -1
        life -= 1
        hud_score.clear()
        hud_score.write(f"{score}", align="center",
                        font=("Press Start 2P", 24, "normal"))
        hud_life.clear()
        hud_life.write(f"{life}", align="center",
                       font=("Press Start 2P", 24, "normal"))
        playsound("bounce.wav")

    for i in block_list:
        if ball.xcor() + 10 >= i.xcor() - 10 and\
           ball.xcor() - 10 <= i.xcor() + 10:
            if ball.ycor() >= i.ycor() - 5 and\
               ball.ycor() <= i.ycor() + 5:
                ball.dy *= -1
                i.goto(1000, 1000)
                print(i.color())

                if (i.color()[0] == 'red'):
                    score += 7
                elif (i.color()[0] == 'orange'):
                    score += 5
                elif (i.color()[0] == 'green'):
                    score += 3
                elif (i.color()[0] == 'yellow'):
                    score += 1

                block_count -= 1

                hud_score.clear()
                hud_score.write(f"{score}", align="center",
                                font=("Press Start 2P", 24, "normal"))
                hud_life.clear()
                hud_life.write(f"{life}", align="center",
                               font=("Press Start 2P", 24, "normal"))
                playsound("bounce.wav")

    if life == 0:
        screen.clear()
        screen.bgcolor("black")
        hud_score.clear()
        hud_score.goto(0, 0)
        hud_score.write(f'GAME OVER\nScore: {score}', align='center',
                        font=("Press Start 2P", 24, "normal"))
        playsound("game-over.wav")
        break

turtle.mainloop()
