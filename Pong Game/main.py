from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from math import sqrt

GAME_END_SCORE = 10
CURRENT_SCORE = 0
X_MAX = 390
X_MIN = -390
ORIGIN = (0, 0)

screen = Screen()
screen.tracer(0)
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
left_paddle = Paddle(x_pos=-380, y_pos=0, color_choice="sky blue")
right_paddle = Paddle(x_pos=380, y_pos=0, color_choice="yellow")
ball_of_the_game = Ball()
scoreboard = Scoreboard()
screen.update()
screen.tracer(1)
screen.listen()
game_is_being_played = True
screen.onkeypress(key="Up", fun=right_paddle.up)
screen.onkeypress(key="Down", fun=right_paddle.down)
screen.onkeypress(key="w", fun=left_paddle.up)
screen.onkeypress(key="s", fun=left_paddle.down)
while game_is_being_played:
    if CURRENT_SCORE == GAME_END_SCORE:
        game_is_being_played = False
    ball_of_the_game.move()
    if ball_of_the_game.ycor() > 290 or ball_of_the_game.ycor() < -290:

        ball_of_the_game.bounce()
    if (ball_of_the_game.xcor() > 360 and ball_of_the_game.distance(right_paddle) < sqrt(2900)) or (
            ball_of_the_game.xcor() < -360 and ball_of_the_game.distance(left_paddle) < sqrt(2900)):
        ball_of_the_game.add_speed()
        ball_of_the_game.reverse()
    if ball_of_the_game.xcor() > X_MAX:
        screen.tracer(0)
        ball_of_the_game.setpos(ORIGIN)
        ball_of_the_game.reset_speed()
        ball_of_the_game.reverse()
        scoreboard.add_l()
        screen.tracer(1)
        CURRENT_SCORE += 1

    elif ball_of_the_game.xcor() < X_MIN:
        screen.tracer(0)
        ball_of_the_game.setpos(ORIGIN)
        ball_of_the_game.reset_speed()
        ball_of_the_game.reverse()
        scoreboard.add_r()
        screen.tracer(1)
        CURRENT_SCORE += 1


screen.exitonclick()
