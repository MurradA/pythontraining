import turtle
import random

colours = ["blue", "black", "yellow", "red", "green", "purple"]

turtle.pensize(3)

for i in range(0, 8):
    turtle.color(random.choice(colours))
    turtle.forward(50)
    turtle.right(45)

turtle.exitonclick()
