import time
from turtle import Screen
from pongscreen import PongScreen
from paddle import Paddle
from ball import Ball
from score import Score

screen = Screen()
screen.setup(width=900, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
screen.listen()

pong_layout = PongScreen()

player_1 = Paddle()
player_1.create_paddle("left")
player_1_score = Score()
screen.onkey(player_1.turn_up, "q")
screen.onkey(player_1.turn_down, "a")

player_2 = Paddle()
player_2.create_paddle("right")
player_2_score = Score()
player_2_score.show_score("left")
screen.onkey(player_2.turn_up, "Up")
screen.onkey(player_2.turn_down, "Down")

ball = Ball()

is_playing = True
while is_playing:
    player_1_score.show_score("right")
    player_2_score.show_score("left")
    
    screen.update()
    ball.move_ball()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_wall()

    if ball.xcor() >= 370 and ball.distance(player_2) < 40:
        ball.bounce_paddle()
    elif ball.xcor() >= 370:
        ball.restart()
        player_1_score.add_point()

    if ball.xcor() <= -370 and ball.distance(player_1) < 40:
        ball.bounce_paddle()
    elif ball.xcor() <= -370:
        ball.restart()
        player_2_score.add_point()
        
    if player_1_score == 10 or player_2_score == 10:
        is_playing = False


screen.exitonclick()
