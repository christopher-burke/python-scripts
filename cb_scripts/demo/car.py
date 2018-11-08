#!/usr/bin/env python3

"""Car class.

Show the uses of __repr__ and __str__.
"""


class Car:
    def __init__(self, color, mileage, *args, **kwargs):
        self.color = color
        self.mileage = mileage

    def __repr__(self):
        return f'Car(color={self.color}, mileage={self.mileage})'

    def __str__(self):
        return f'a car {self.color} car'


if __name__ == "__main__":
    my_car = Car('blue', 3451)

    # __str__ called:
    print(my_car)

    # __repr__ called:
    print(repr(my_car))
