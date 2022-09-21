from turtle import Turtle
import time

class ball(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.shapesize(1,1)
        self.x_cor = 10
        self.y_cor = 10
        self.move_speed = 0.1

    def move(self):
            new_ycor = self.ycor() + self.y_cor
            new_xcor = self.xcor() + self.x_cor
            self.goto(new_xcor,new_ycor)

    def bounce1(self):
        self.y_cor *= -1
        

    def bounce_x(self):
        self.x_cor *= -1
        self.move_speed *= 0.5

        
    def reset_position(self):
        self.goto(0,0)
        self.move_speed = 0.1
        self.bounce1()