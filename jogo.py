import random
import turtle


def Init_Player_One(color):
    player = turtle.Turtle()
    player.shape("turtle")
    player.color(color)
    player.penup()
    player.goto(-200, 100)
    return player


def Init_Player_Two(color):
    player = player_one.clone()
    player.color(color)
    player.penup()
    player.goto(-200, -100)
    return player


def Walke_To_Board(player, x_start, y_start, x_end, y_end):
    player.goto(x_start, y_start)
    player.pendown()
    player.circle(40)
    player.penup()
    player.goto(x_end, y_end)


def Get_Player_Die_Outcome(player):
    player_one_turn = input("Press 'Enter' to roll the die ")
    die_outcome = random.choice(die)
    print("The result of the die roll is: ")
    print(die_outcome)
    print("The number of steps will be: ")
    print(20 * die_outcome)
    return die_outcome


player_one = Init_Player_One("green")

player_two = Init_Player_Two("blue")

Walke_To_Board(player_one, 300, 60, -200, 100)

Walke_To_Board(player_two, 300, -140, -200, -100)

die = [1, 2, 3, 4, 5, 6]
for i in range(20):
    if player_one.pos() >= (300, 100):
        print("Player One Wins!")
        break
    elif player_two.pos() >= (300, -100):
        print("Player Two Wins!")
        break
    else:
        die_outcome_one = Get_Player_Die_Outcome(player_one)
        player_one.fd(20 * die_outcome_one)
        die_outcome_two = Get_Player_Die_Outcome(player_two)
        player_two.fd(20 * die_outcome_two)
