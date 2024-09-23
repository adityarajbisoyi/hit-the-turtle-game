from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("turtle")
        self.penup()
        self.direction_vector_of_x = 1
        self.direction_vector_of_y = 1

    def move(self):
        x_pos = self.xcor() + self.direction_vector_of_x
        y_pos = self.ycor() + self.direction_vector_of_y
        self.setpos(x_pos, y_pos)

    def bounce(self):
        self.direction_vector_of_y *= -1

    def reverse(self):
        self.direction_vector_of_x *= -1

    def add_speed(self):
        if self.direction_vector_of_x > 0:
            self.direction_vector_of_x += 0.5
            if self.direction_vector_of_y > 0:
                self.direction_vector_of_y += 0.5
            else:
                self.direction_vector_of_y -= 0.5
        else:
            self.direction_vector_of_x -= 0.5
            if self.direction_vector_of_y > 0:
                self.direction_vector_of_y += 0.5
            else:
                self.direction_vector_of_y -= 0.5

    def reset_speed(self):
        self.direction_vector_of_y /= self.direction_vector_of_y
        self.direction_vector_of_x /= self.direction_vector_of_x
