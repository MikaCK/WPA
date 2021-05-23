import turtle
import math
import random

def domcek(turtle, px: int = 0, py: int = 0) -> None:
    """Draw domcek on px and py

    :param turtle: domcel
    :param px: suradnica x
    :param py: suradnica y
    :return: None
    """
    c = math.sqrt(100**2 + 100**2)
    t.fd(-100)
    t.lt(45)
    t.fd(c)
    t.rt(45)
    t.fd(-100)
    t.rt(45)
    t.fd(c)
    t.lt(135)
    t.fd(100)
    t.lt(45)
    t.fd(75)
    t.lt(90)
    t.fd(75)
    t.lt(45)
    t.fd(100)

    t.pu()
    t.setpos(px, py)
    t.setheading(random.randrange(360))
    t.pd()

t = turtle.Turtle()
t.pensize(3)

for _ in range(6):
    t.pencolor(f'#{random.randrange(256 ** 3):06x}')
    px = random.randint(-500, 500)
    py = random.randint(-500, 500)
    domcek(t, px, py)

domcek(t)
turtle.mainloop()

