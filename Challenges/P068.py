import turtle
import random

lines = random.randint(5,20)

for x in range(0 , lines):
    length = random.randint(25, 100)
    rotate = random.randint(1, 365)
    turtle.forward(length)
    turtle.right(rotate)


turtle.exitonclick()

# import turtle
# import random
#
# lines = random.randint(5,20)
# for i in range(0, lines + random.randint(0,5)):
#     for x in range(0, lines):
#         length = random.randint(25, 100)
#         rotate = random.randint(1, 365)
#         turtle.forward(length)
#         turtle.right(rotate)
#     turtle.left(random.randint(0, 45))
#
#
# turtle.exitonclick()