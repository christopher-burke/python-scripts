import unittest
from divisors import prime, divisors


class TestDivisors(unittest.TestCase):

    def setUp(self):
        pass

    def test_prime_89(self):
        self.assertEqual(prime(89), True)

    def test_prime_1(self):
        self.assertFalse(prime(1), False)

    def test_divisors_88(self):
        self.assertEqual(divisors(88), [1, 2, 4, 8, 11, 22, 44, 88])

    def test_divisors_127(self):
        self.assertEqual(divisors(127), [1, 127])

    def test_divisors_6(self):
        self.assertNotEqual(divisors(6), [1, 2, 3, 7])


if __name__ == '__main__':
    unittest.main()
