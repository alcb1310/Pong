from turtle import Turtle

SELECTED_FONT = ('Courier', 50, 'normal')


class Score(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 240)
        self.color("white")
        
    def add_point(self) -> None:
        self.score += 1
        
    def show_score(self, alignment):
        self.clear()
        self.write(arg=f"   {self.score}   ",  align=alignment, move=False, font=SELECTED_FONT)