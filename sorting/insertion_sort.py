#!/usr/bin/env python3

"""Insertion Sort."""


import copy


def insertion_sort(A):
    """Insertion sort algorithm implementation."""
    for j in range(1, len(A)):
        key = copy.deepcopy(A[j])
        i = j
        while i > 0 and A[i-1] > key:  # Zero indexed
            A[i] = A[i-1]
            i = i - 1
        A[i] = key
    return A


if __name__ == "__main__":
    insertion_sort([5, 2, 4, 6, 1, 3])
