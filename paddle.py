from turtle import Turtle

class Paddle(Turtle):
    
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)



# screen.listen()
# screen.onkey(go_up, "Up")
# screen.onkey(go_down, "Down")
#
# game_is_on = True
# while game_is_on:
#     screen.update()