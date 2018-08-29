import unittest
from two_sum import two_sums, two_sums_brute_force


class TestTwoSums(unittest.TestCase):

    def setUp(self):
        self.nums = [2, 7, 11, 15]
        self.target = 9
        self.wrong_target = 8

    def test_two_sums(self):
        test = two_sums(nums=self.nums, target=self.target)
        self.assertNotEqual(test, 'No two sum solution')
        self.assertEqual(test, '[0, 1]')

    def test_two_sums_not_found(self):
        test = two_sums(nums=self.nums, target=self.wrong_target)
        self.assertNotEqual(test, '[0, 1]')
        self.assertEqual(test, 'No two sum solution')

    def test_two_sums_brute_force(self):
        self.assertEqual(two_sums_brute_force(
            nums=self.nums, target=self.target), '[0, 1]')


if __name__ == '__main__':
    unittest.main()
