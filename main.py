import time
from turtle import Screen
from pongscreen import PongScreen
from paddle import Paddle
from ball import Ball

screen = Screen()
screen.setup(width=900, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
screen.listen()

pong_layout = PongScreen()

player_1 = Paddle()
player_1.create_paddle("left")
screen.onkey(player_1.turn_up, "q")
screen.onkey(player_1.turn_down, "a")

player_2 = Paddle()
player_2.create_paddle("right")
screen.onkey(player_2.turn_up, "Up")
screen.onkey(player_2.turn_down, "Down")

ball = Ball()

is_playing = True
while is_playing:
    screen.update()
    ball.move_ball()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_wall()

    if ball.xcor() >= 370 and ball.distance(player_2) < 40:
        ball.bounce_paddle()
    elif ball.xcor() >= 370:
        ball.restart()
        screen.update()
        time.sleep(0.5)

    if ball.xcor() <= -370 and ball.distance(player_1) < 40:
        ball.bounce_paddle()
    elif ball.xcor() <= -370:
        ball.restart()
        screen.update()
        time.sleep(0.5)


screen.exitonclick()
