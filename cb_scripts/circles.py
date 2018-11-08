#!/usr/bin/env python3

""""""

from math import pi as π
from typing import Union


def checker(func):
    """Decorator to check the inputs are valid.

    Uses the CheckCircleInputs class to determine if the radius
    input is valid.
    """
    def wrapper(*args, **kwargs):
        CheckCircleInputs(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper


@checker
def circle_circumference(radius: Union[int, float]):
    """Calculate the circumference of a circle."""
    return 2 * π * radius


@checker
def circle_area(radius: Union[int, float]):
    """Calculate the area of a circle."""
    return π * (radius**2)


class CheckCircleInputs:

    def __init__(self, *args, **kwargs):
        radius = None
        if args:
            radius = args[-1]
        if 'radius' in kwargs:
            radius = kwargs['radius']
        self.type_check(radius)
        self.value_check(radius)

    def type_check(self, radius):
        if type(radius) not in [int, float]:
            raise TypeError(
                f"Radius must be a number. Input was type(radius)={type(radius)}")

    def value_check(self, radius):
        if radius < 0:
            raise ValueError(
                f"Radius cannot be negative. Input was radius={radius}.")


class Circle:
    @checker
    def __init__(self, radius:  Union[int, float]):
        self.radius = radius

    def circle_circumference(self):
        return 2 * π * self.radius

    def circle_area(self):
        return π * (self.radius**2)
