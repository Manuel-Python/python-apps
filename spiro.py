import turtle as t
import random

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r,g,b)

tur = t.Turtle()
t.colormode(255)
# directions = [0, 90, 180, 270]
# tur.pensize(15)
tur.speed(0)

for _ in range(400):
    current_heading = tur.heading()
    tur.setheading(current_heading + 5)
    tur.color(random_color())
    tur.circle(100)




screen = t.screen()
screen.exitonclick()