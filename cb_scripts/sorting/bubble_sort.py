#!/usr/bin/env python3


"""Bubble Sort."""


def swap(value1, value2):
    """Return the value1 and value2 swapped.

    return tuple (value2, value1)
    """
    return (value2, value1,)


def bubble_sort(array):
    """Bubble sort sorting algorthim implementation.

    Algorthimic complexity Big O(n^2).
    """
    for _ in range(len(array)):
        for element in enumerate(array):
            i = element[0]
            try:
                if array[i] > array[i+1]:
                    array[i], array[i+1] = swap(array[i], array[i+1])
            except IndexError:
                pass  # Reached the end of the Array
    return array


if __name__ == "__main__":
    print(bubble_sort([15, 30, 21, 44, 11]))
    print(bubble_sort([100, 500, 300, 200, 400]))
