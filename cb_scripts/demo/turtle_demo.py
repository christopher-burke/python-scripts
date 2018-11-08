#!/usr/bin/env python3

"""Demo of the turtule module."""

import turtle

t = turtle.Turtle()

# Draw square spiral
for i in range(500):
    t.forward(i)
    t.left(91)
