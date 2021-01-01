from turtle import Turtle, Screen
import random

def dist():
    return random.randint(0,10)

def win(turtle):
    if turtle.xcor() > 230:
        return True
    else:
        return False

screen = Screen()
screen.setup(width=500, height=500)
#user_pick = screen.textinput(title="Colour", prompt="Turtle colour")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

t1 = Turtle(shape="turtle")
t1.color(colors[0])
t1.penup()
t1.goto(x=-230, y=-100)

t2 = Turtle(shape="turtle")
t2.color(colors[1])
t2.penup()
t2.goto(x=-230, y=-70)

t3 = Turtle(shape="turtle")
t3.color(colors[2])
t3.penup()
t3.goto(x=-230, y=-40)

t4 = Turtle(shape="turtle")
t4.color(colors[3])
t4.penup()
t4.goto(x=-230, y=-10)

t5 = Turtle(shape="turtle")
t5.color(colors[4])
t5.penup()
t5.goto(x=-230, y=20)

t6 = Turtle(shape="turtle")
t6.color(colors[5])
t6.penup()
t6.goto(x=-230, y=50)

while True:
   t1.forward(dist())
   if win(t1):
       print(t1.pencolor())
       break
   t2.forward(dist())
   if win(t2):
       print(t2.pencolor())
       break
   t3.forward(dist())
   if win(t3):
       print(t3.pencolor())
       break
   t4.forward(dist())
   if win(t4):
       print(t4.pencolor())
       break
   t5.forward(dist())
   if win(t5):
       print(t5.pencolor())
       break
   t6.forward(dist())
   if win(t6):
       print(t6.pencolor())
       break

screen.exitonclick()

