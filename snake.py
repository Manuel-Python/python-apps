from turtle import Screen, Turtle
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Nokia Snake")
screen.tracer(0)


starting_positions = [(0,0), (-20,0), (-40,0)]
segments = []

for postion in starting_positions:
    segment = Turtle("square")
    segment.color("white")
    segment.penup()
    segment.goto(postion)
    segments.append(segment)

screen.update()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    for segnum in range(len(segments)-1,0,-1):
        new_x = segments[segnum - 1].xcor()
        new_y = segments[segnum - 1].ycor()
        segments[segnum].goto(new_x,new_y)
    segments[0].forward(20)

# segment_1 = Turtle("square")
# segment_1.color("white")
#
# segment_2 = Turtle("square")
# segment_2.color("white")
# segment_2.goto(-20,0)
#
# segment_3 = Turtle("square")
# segment_3.color("white")
# segment_3.goto(-40,0)






screen.exitonclick()