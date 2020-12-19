#!/usr/bin/env python3
# coding:utf-8
import turtle

turtle.down()
a = 0
for loop in range(50):
    turtle.forward(100 - a)
    turtle.left(90)
    a += 2

turtle.exitonclick()
