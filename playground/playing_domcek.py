import turtle
import math
import random

def posun():
    t.pu()
    t.setpos(random.randint(-300, 300), random.randint(-200, 200) )
    t.setheading(random.randrange(360))
    t.pd()


def domcek(a):
    #t.fillcolor(f'#{random.randrange(256**3):06x}')
    c = math.sqrt(100 ** 2 + 100 ** 2)
    turtle.fd(-100)
    turtle.lt(45)
    turtle.fd(c)
    turtle.rt(45)

    turtle.fd(-100)
    turtle.lt(45)
    turtle.fd(75)
    turtle.rt(90)

    turtle.fd(75)
    turtle.rt(45)

    turtle.fd(100)
    turtle.rt(135)
    turtle.fd(c)
    turtle.lt(135)
    turtle.fd(100)

t = turtle.Turtle()
for i in range(10):
    posun()
    domcek(random.randint(30, 100))


turtle.mainloop()