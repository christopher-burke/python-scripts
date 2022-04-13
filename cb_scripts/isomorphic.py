#!/usr/bin/env python3

"""Isomorphic strings."""


from collections import Counter


def isomorphic(string_1: str, string_2: str) -> bool:
    """"Isomorphic string checker."""
    s1_count = Counter(string_1)
    s2_count = Counter(string_2)
    iso_matches = [i == k for i, k in zip(
        sorted(s1_count.values()), sorted(s2_count.values()))]
    return all(iso_matches)


def main():
    """Run test cases."""
    assert isomorphic("foo", "bar") is False
    assert isomorphic("egg", "odd") is True
    assert isomorphic("paper", "title") is True
    print('Passed.')


if __name__ == "__main__":
    main()
