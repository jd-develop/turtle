#!/usr/bin/env python3
# coding:utf-8
import turtle
import random

turtle.colormode(255)
turtle.up()
turtle.goto(-100, -100)
turtle.down()
a = 0
for loop in range(100):
    turtle.forward(200 - a)
    turtle.left(90)
    R = random.randrange(0, 257, 10)
    B = random.randrange(0, 257, 10)
    G = random.randrange(0, 257, 10)
    turtle.color((R, G, B))
    a += 2
turtle.up()
turtle.goto(1000, 1000)

turtle.exitonclick()
