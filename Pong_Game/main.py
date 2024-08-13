import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

GAME_ON = True


def end_game():
    GAME_ON = False


screen = Screen()
screen.setup(height=600,width=800)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

player_1 = Paddle(1)
player_2 = Paddle(2)
ball = Ball()
scoreboard = Scoreboard()

screen.onkey(player_1.move_up, "w")
screen.onkey(player_1.move_down, "s")
screen.onkey(player_2.move_up, "Up")
screen.onkey(player_2.move_down, "Down")
screen.onkey(end_game, "b")

screen.listen()

scoreboard.draw_screen()

while GAME_ON:
    screen.update()
    ball.move_ball()

    if ball.ycor() < -280 or ball.ycor() > 280:
        ball.bounce_y()

    if (ball.xcor() < -320 and ball.distance(player_1) < 50) or (ball.xcor() > 320 and ball.distance(player_2) < 50):
        ball.bounce_x()

    if ball.xcor() < -380 or ball.xcor() > 380:
        scoreboard.make_point(ball.xcor())
        ball.reset_position()

    time.sleep(ball.move_speed)

