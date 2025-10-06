# Intentional linting issues for testing

# import os, sys


VARIABLE_ONE = 1
VARIABLE_TWO = 2


def test_function(x, y):
    z = x + y
    print("Sum is", z)
    return z


UNUSED_VARIABLE = 42

if True:
    print("This line is fine")
    print("This line has bad indentation")

LONG_LINE = "This is a very long line that will exceed the 88 character \
limit that Black enforces in default configuration"


def add_numbers(a: int, b: int) -> int:
    """Adds two numbers."""
    return a + b


# Missing docstring
def subtract(a, b):
    return a - b
