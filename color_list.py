import colorgram
import turtle as t
import random



t.colormode(255)
ti = t.Turtle()

def move_forward():
    ti.forward(10)

def move_backwards():
    ti.backward(10)

def turn_right():
    new_heading = ti.heading() -10
    ti.setheading(new_heading)

def turn_left():
    new_heading = ti.heading() + 10
    ti.setheading(new_heading)

def clear():
    ti.clear() #clear this turtles graphics
    ti.penup()
    ti.home()
    ti.pendown()

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     #rgb_colors.append(color.rgb)
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     extract = (r,g,b)
#     rgb_colors.append(extract)

#print(rgb_colors)

color_list = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123),
              (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35),
              (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77),
              (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102),
              (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

#print(color_list)

t.setheading(225)
t.forward(300)
t.setheading(0)
t.speed(0)

num_dots = 20

for dot_count in range(1, num_dots+1):
    t.dot(20, random.choice(color_list))
    t.forward(50)
    if dot_count % 10 == 0:
        t.setheading(90)
        t.forward(50)
        t.setheading(180)
        t.forward(500)
        t.setheading(0)

t.hideturtle()
screen = t.Screen()
screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear)
screen.exitonclick()
