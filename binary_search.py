#!/usr/bin/env python3


"""Binary Search Algorithm implmentation."""


def binary_search(items, value, low: int, high: int):
    """Binary Search an iterable for a value and return the position.

    Recursive Binary Serach (https://rosettacode.org/wiki/Binary_search):

    // initially called with low = 0, high = N - 1
    BinarySearch_Left(A[0..N-1], value, low, high) {
      // invariants: value > A[i] for all i < low
                     value <= A[i] for all i > high
      if (high < low)
          return low
      mid = (low + high) / 2
      if (A[mid] >= value)
          return BinarySearch_Left(A, value, low, mid-1)
      else
          return BinarySearch_Left(A, value, mid+1, high)
    }
    """
    if (high < low):
        return -1
    mid = (low + high) // 2
    if(items[mid] > value):
        return binary_search(items, value, low, mid-1)
    elif(items[mid] < value):
        return binary_search(items, value, mid+1, high)
    else:
        return mid


def helper(items, value):
    """Binary Search helper function."""
    return binary_search(items, value, low=0, high=len(items))


if __name__ == "__main__":
    nums = [9, 1, 2, 3, 4, 6, 5, 7, 8, ]
    nums = sorted(nums)
    assert (binary_search(nums, 2, 0, len(nums)-1) == 2) is False
    assert (binary_search(nums, 7, low=0, high=len(nums)-1) == 6) is True
    assert (binary_search(nums, 1, 0, len(nums)-1) == 0) is True
    assert (binary_search(nums, 7, low=0, high=len(nums)-1) == 6) is True
    assert (binary_search(nums, 5, low=0, high=len(nums)-1) == 4) is True
    assert (binary_search(nums, 9, low=0, high=len(nums)-1) == 8) is True
    assert (helper(nums, 9) == 8) is True
    print("Tests passed.")
