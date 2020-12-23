from turtle import Turtle, Screen #Puppet Master
import random

ti = Turtle()
ti.shape("arrow")
ti.color("salmon1")



# for _ in range(4):
#     ti.forward(100)
#     ti.left(90)

# for _ in range(15):
#     ti.forward(10)
#     ti.penup()
#     ti.forward(10)
#     ti.pendown()

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen",
           "wheat", "SlateGray", "SeaGreen"]

ti.penup()

ti.right(270)
ti.forward(100)

ti.pendown()

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        ti.forward(100)
        ti.right(angle)

for x in range(3,15):
    ti.color(random.choice(colours))
    draw_shape(x)

screen = Screen()
screen.exitonclick()

