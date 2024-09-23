from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_pos, y_pos, color_choice):
        super().__init__()
        self.shape("square")
        self.color(color_choice)
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.penup()
        self.setpos(x=x_pos, y=y_pos)
        self.setheading(90)

    def up(self):
        if self.ycor() < 225:
            self.forward(40)

    def down(self):
        if self.ycor() > -225:
            self.backward(40)
