#!/usr/bin/env python3


"""Merge Sort."""


def merge(a, b):
    """Function to merge two arrays in order."""
    sorted_array = []
    while len(a) != 0 and len(b) != 0:
        if a[0] < b[0]:
            sorted_array.append(a[0])
            a.remove(a[0])
        else:
            sorted_array.append(b[0])
            b.remove(b[0])

    if len(a) == 0:
        sorted_array.extend(b)
    else:
        sorted_array.extend(a)
    return sorted_array


def merge_sort(array):
    """Merge sort.

    Algorthimic complexity Big O(n lg n).
    """

    length = len(array)
    if length <= 1:
        return array

    l1 = merge_sort(array[:length//2])
    l2 = merge_sort(array[length//2:])

    return merge(l1, l2)


if __name__ == "__main__":
    print(merge_sort([15, 30, 21, 44, 11]))
    print(merge_sort([100, 500, 300, 200, 400]))
