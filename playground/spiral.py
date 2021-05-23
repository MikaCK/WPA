import turtle
import random

t = turtle.Turtle()
t.speed(0)
uhol = random.randint(20, 170)
print('uhol=', uhol)

for d in range(10, 300, 3):
    t.fd(d)
    t.lt(uhol)