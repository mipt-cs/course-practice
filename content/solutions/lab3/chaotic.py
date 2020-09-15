#!/bin/env python3

from record import start, finish
import turtle
from random import randint
#import sys

width = 300
height = 300

start(width, height, 0, 0, 50, __file__)

turtle.speed(5)
turtle.color('red')

for step in range(100):
    turtle.right(randint(-180, 179))
    turtle.forward(randint(5, 50))

finish()
