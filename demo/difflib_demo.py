#!/usr/bin/env python3

"""Example of difflib."""


from difflib import context_diff


a_list = ['1', '2', '3', '4']
b_list = ['-2', '0', '2', '4', '6']


if __name__ == "__main__":
    for x in context_diff(a=a_list, b=b_list):
        print(x)
