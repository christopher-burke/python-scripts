#!/usr/bin/env python3


"""Test for flatten module."""


import unittest
from flatten import flatten, flatten_as_list, flatten_as_tuple


class TestFlatten(unittest.TestCase):
    """Test for the flatten module."""

    @classmethod
    def setUpClass(self):
        """Create a sample var with a list of lists.

        This sample value will be used for the tests.
        """
        self.sample = [[1, 2, 3], [4, 5, 6], [7]]
        self.correct = [1, 2, 3, 4, 5, 6, 7]

    def test_flatten(self):
        """Test for flatten function."""
        self.assertEqual(list(flatten(self.sample)),
                         self.correct)

    def test_flatten_as_list(self):
        """Test for flatten_as_list function."""
        self.assertEqual(flatten_as_list(self.sample), self.correct)

    def test_flatten_as_tuple(self):
        """Test for flatten_as_tuple function."""
        self.assertEqual(flatten_as_tuple(self.sample), tuple(self.correct))


if __name__ == '__main__':
    unittest.main()
