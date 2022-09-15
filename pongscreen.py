from turtle import Turtle


class PongScreen(Turtle):
    def __init__(self):
        super().__init__()

        self.hideturtle()
        self.color("white")
        self.penup()
        self.pensize(10)
        self.goto((0, 250))
        self.setheading(270)
        while self.ycor() > -250:
            self.pendown()
            self.fd(20)
            self.penup()
            self.fd(20)
