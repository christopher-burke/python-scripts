#!/usr/bin/env python3

"""Monkey Patching - dynamically modify a class or module at runtime."""


class MyClass:
    def my_method():
        print('My Method.')


def monkey_patch():
    print('Monkey patch method.')


def main():
    m = MyClass()
    m.my_method = monkey_patch
    m.my_method()


if __name__ == "__main__":
    main()
    print('Changes in the behavior of my_method in MyClass using'
          ' the function monkey_patch().')
