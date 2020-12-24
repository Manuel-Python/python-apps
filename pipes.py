from turtle import Turtle, Screen #Puppet Master
import random

ti = Turtle()
ti.shape("arrow")
ti.color("salmon1")

colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen",
           "wheat", "SlateGray", "SeaGreen"]

directions = [0, 90, 180, 270]

ti.penup()

ti.right(270)
ti.forward(200)

ti.pendown()

ti.pensize(15)
ti.speed("fastest")

for _ in range(200):
    ti.color(random.choice(colors))
    ti.forward(30)
    ti.setheading(random.choice(directions))

screen = Screen()
screen.exitonclick()

