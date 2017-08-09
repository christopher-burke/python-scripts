
#!/usr/bin/python

__author__ = "Christopher J. Burke"
__email__ = "christopherjamesburke@gmail.com"

def fizz_buzz(input_number, fizz=3, buzz=5):
    output = ""
    if input_number % fizz == 0:
        output +="Fizz"
    if input_number % buzz == 0:
        output += "Buzz"
    if not output:
        output = input_number
    return output


if __name__ == "__main__":
    for input_number in range(1,101):
        print(fizz_buzz(input_number,fizz=3, buzz=5))
