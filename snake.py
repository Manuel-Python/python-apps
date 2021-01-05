from turtle import Screen, Turtle

STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20

class Snake:

        def __init__(self):
            self.segments = []
            self.create_snake()
            self.head = self.segments[0]

        def create_snake(self):
            for postion in STARTING_POSITIONS:
                segment = Turtle("square")
                segment.color("white")
                segment.penup()
                segment.goto(postion)
                self.segments.append(segment)

        def move(self):
            for segnum in range(len(self.segments)-1,0,-1):
                new_x = self.segments[segnum - 1].xcor()
                new_y = self.segments[segnum - 1].ycor()
                self.segments[segnum].goto(new_x,new_y)
            self.head.forward(MOVE_DISTANCE)

        def up(self):
            self.head.setheading(90)

        def down(self):
            self.head.setheading(270)

        def left(self):
            self.head.setheading(180)

        def right(self):
            self.head.setheading(0)