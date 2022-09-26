import turtle as t
import random

# screen = t.Screen()
# screen.exitonclick()

chris = t.Turtle()
t.colormode(255)

radius = 50


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)

    return color


for _ in range(100):
    chris.speed("normal")
    chris.color(random_color())
    chris.circle(100)
    chris.setheading(chris.heading() + 10)

