#!/usr/bin/python

"""FizzBuzz Test.

FizzBuzz Test:
Write a program that prints the numbers from 1 to 100.
But for multiples of three print Fizz instead of the number
and for the multiples of five print Buzz.
For numbers which are multiples of both three and five print FizzBuzz
"""

def fizz_buzz(input_number, fizz=3, buzz=5):
    """Fizz Buzz function.

    input_number: number being tested.
    fizz: multiple should be replaced by fizz. Default 3.
    buzz: multiple should be replaced by buzz. Default 5.
    """
    output = ""
    if input_number % fizz == 0:
        output += "Fizz"
    if input_number % buzz == 0:
        output += "Buzz"
    if not output:
        output = input_number
    return output


if __name__ == "__main__":
    for input_number in range(1, 101):
        print(fizz_buzz(input_number, fizz=3, buzz=5))
