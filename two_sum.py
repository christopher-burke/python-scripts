#!/usr/bin/env python3

"""Two Sums.

Given an array of integers, return indices of the two
numbers such that they add up to a specific target.

You may assume that each input would have exactly
one solution, and you may not use the same element twice.

https://leetcode.com/problems/two-sum/description/
"""


def two_sums_brute_force(nums, target, *args, **kwargs):
    """Return the two indices in nums that add up to target.

    This is a Brute force method.
    """
    for i in nums:
        for j in nums[1:]:
            if i + j == target:
                return f'[{nums.index(i)}, {nums.index(j)}] '


def two_sums(nums, target, *args, **kwargs):
    """Return the two indices in nums that add up to target.

    This uses python dictionaries.
    """
    map_ = dict(zip(nums, range(len(nums))))

    for key, value in map_.items():
        complement = target - key
        if complement in map_.keys():
            return f'[{value} {map_[complement]}]'

    return f'No two sum solution'


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    print(two_sums_brute_force(**locals()))
    print(two_sums(**locals()))
