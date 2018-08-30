import unittest
from breathe import breathe


class TestBreathe(unittest.TestCase):
    """Unittest TestCase for Circle."""

    def test_breathe(self):
        """Test areas. radius >= 0."""
        self.assertEqual(breathe(-1, -1), None)


if __name__ == '__main__':
    unittest.main()
