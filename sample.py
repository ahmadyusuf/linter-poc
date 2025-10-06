# Intentional linting issues for testing

# import os, sys


vairableOne = 1
variable_two = 2

def testFunction(x, y):
    z = x + y
    print("Sum is", z)
    return z


unused_var = 42

if True:
    print("This line is fine")
    print("This line has bad indentation")

long_line = "This is a very long line that will exceed the 88 character \
limit that Black enforces in default configuration"


def add_numbers(a: int, b: int) -> int:
    """Adds two numbers."""
    return a + b


# Missing docstring
def subtract(a, b):
    return a - b
