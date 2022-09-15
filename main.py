from turtle import Screen
from pongscreen import PongScreen


screen = Screen()
screen.setup(width=800, height=500)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

pong_layout = PongScreen()
screen.update()

screen.exitonclick()
