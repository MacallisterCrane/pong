from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color('green')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def p_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def p_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)