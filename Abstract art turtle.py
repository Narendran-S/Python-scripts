# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 16:34:49 2020

@author: kiddy
"""


import turtle
wn = turtle.Screen()
alex = turtle.Turtle()
dist = 10
angle = 10
turtle.speed(0)
for _ in range(175):
    turtle.forward(dist)
    turtle.left(angle)
    dist += 1
    angle += 1
    wn.exitonclick()