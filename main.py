from turtle import Screen
from pongscreen import PongScreen
from paddle import Paddle

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

is_playing = True
while is_playing:
    screen.update()

screen.exitonclick()
