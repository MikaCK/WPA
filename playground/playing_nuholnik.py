import turtle
import random


def nuholnik(n, a):
    for i in range(n):
        t.fd(a)
        t.right(360 / n)


def stvrt(a):
    for i in range(9):
        t.fd(a)
        t.right(10)


def lupen(a):
    for i in range(2):
        stvrt(a)
        t.right(90)


t = turtle.Turtle()
t.speed(0)

# for n in range(3, 15):
#     nuholnik(n, 100)
