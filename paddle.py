from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()

    def turn_up(self):
        if self.ycor() < 280:
            self.setheading(90)
            self.forward(20)

    def turn_down(self):
        if self.ycor() > -280:
            self.setheading(270)
            self.forward(20)

    def create_paddle(self, position):
        """
        :param position: string left or right
        when left is passed then the paddle will be created at the left of the screen and if right was passed then
        it will be created at the left
        """
        self.shape("square")
        self.shapesize(stretch_len=4)
        self.setheading(90)
        self.color("white")
        if position == "left":
            self.goto(-380, 0)
        elif position == "right":
            self.goto(380, 0)

