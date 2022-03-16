#!/usr/bin/env python3

"""Unittest for circles.py."""


import unittest
from circles import circle_area, circle_circumference
from math import pi as π


class TestCircleArea(unittest.TestCase):
    """Unittest TestCase for Circle."""

    def test_area(self):
        """Test areas. radius >= 0."""
        self.assertAlmostEqual(circle_area(1), π)
        self.assertAlmostEqual(circle_area(radius=1), π)
        self.assertAlmostEqual(circle_area(0), 0)
        self.assertAlmostEqual(circle_area(2.1), π * 2.1**2)

    def test_values(self):
        """Test values of radii, ensure value errors are raised."""
        self.assertRaises(ValueError, circle_area, -2)

    def test_types(self):
        """Test types of radii, ensure type errors are raised."""
        self.assertRaises(TypeError, circle_area, 2+5j)
        self.assertRaises(TypeError, circle_area, True)
        self.assertRaises(TypeError, circle_area, "maths")


class TestCircleCircumference(unittest.TestCase):
    """Unittest TestCase for Circle."""

    def test_circumference(self):
        """Test circumference radius >= 0."""
        self.assertAlmostEqual(
            circle_circumference(1), 6.28319, places=5)
        self.assertAlmostEqual(
            circle_circumference(radius=1), 6.28319, places=5)
        self.assertAlmostEqual(circle_circumference(0), 0)
        self.assertAlmostEqual(circle_circumference(2.1), 13.19469, places=5)

    def test_values(self):
        """Test values of radii, ensure value errors are raised."""
        self.assertRaises(ValueError, circle_circumference, -2)

    def test_types(self):
        """Test types of radii, ensure type errors are raised."""
        self.assertRaises(TypeError, circle_circumference, 2+5j)
        self.assertRaises(TypeError, circle_circumference, True)
        self.assertRaises(TypeError, circle_circumference, "maths")


if __name__ == '__main__':
    unittest.main()
