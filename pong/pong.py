import turtle
import winsound

# draw screen
screen = turtle.Screen()
screen.title("My Pong")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)


def draw_paddle(x_pos):
    paddle = turtle.Turtle()
    paddle.speed(0)
    paddle.shape("square")
    paddle.color("white")
    paddle.shapesize(stretch_wid=5, stretch_len=1)
    paddle.penup()
    paddle.goto(x_pos, 0)
    return paddle


# draw paddle L
paddle_L = draw_paddle(-350)

# draw paddle R
paddle_R = draw_paddle(350)

# draw ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.25
ball.dy = 0.25

# score
score_1 = 0
score_2 = 0

# head-up display
hud = turtle.Turtle()
hud.speed(0)
hud.shape("square")
hud.color("white")
hud.penup()
hud.hideturtle()
hud.goto(0, 260)
hud.write("0 : 0", align="center", font=("Press Start 2P", 20, "normal"))


def paddle_up(paddle):
    y = paddle.ycor()
    new_y = y + 30
    if new_y < 250:
        y += 30
    else:
        y += abs(y - 250)
    paddle.sety(y)


def paddle_down(paddle):
    y = paddle.ycor()
    new_y = y - 30
    if new_y > -250:
        y += -30
    else:
        y += -abs(y + 250)
    paddle.sety(y)


# keyboard
screen.listen()

screen.onkeypress(lambda: paddle_up(paddle_L), "w")
screen.onkeypress(lambda: paddle_down(paddle_L), "s")
screen.onkeypress(lambda: paddle_up(paddle_R), "Up")
screen.onkeypress(lambda: paddle_down(paddle_R), "Down")

while True:
    screen.update()

    # ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # collision with the upper wall
    if ball.ycor() > 290:
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        ball.sety(290)
        ball.dy *= -1

    # collision with lower wall
    if ball.ycor() < -290:
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        ball.sety(-290)
        ball.dy *= -1

    # collision with left wall
    if ball.xcor() < -390:
        score_2 += 1
        hud.clear()
        hud.write("{} : {}".format(score_1, score_2), align="center", font=("Press Start 2P", 20, "normal"))
        winsound.PlaySound("bleep.wav", winsound.SND_ASYNC)
        ball.goto(0, 0)
        ball.dx *= -1

    # collision with right wall
    if ball.xcor() > 390:
        score_1 += 1
        hud.clear()
        hud.write("{} : {}".format(score_1, score_2), align="center", font=("Press Start 2P", 20, "normal"))
        winsound.PlaySound("bleep.wav", winsound.SND_ASYNC)
        ball.goto(0, 0)
        ball.dx *= -1

    # collision with the paddle L
    if -360 < ball.xcor() < -330 and paddle_L.ycor() + 60 > ball.ycor() > paddle_L.ycor() - 60:
        ball.dx = abs(ball.dx)
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    # collision with the paddle R
    if 330 < ball.xcor() < 360 and paddle_R.ycor() + 60 > ball.ycor() > paddle_R.ycor() - 60:
        ball.dx = -1 * abs(ball.dx)
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
