from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.current_speed = 1
        self.speed(self.current_speed)
        self.x_move = 1
        self.y_move = 1

    def move_ball(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_wall(self):
        self.y_move *= -1

    def bounce_paddle(self):
        self.x_move *= -1
        
        if self.x_move < 0:
            self.x_move -= 1
        else:
            self.x_move += 1
        
        if self.y_move < 0:
            self.y_move -= 1
        else:
            self.y_move += 1
        
        self.current_speed += 1
        self.speed(self.current_speed)

    def restart(self):
        self.clear()
        self.goto(0, 0)
        self.bounce_paddle()
        self.bounce_wall()
        if self.x_move < 0:
            self.x_move = -1
        else:
            self.x_move = 1
            
        if self.y_move < 0:
            self.y_move = -1
        else:
            self.y_move = 1
            
        self.speed(1)


