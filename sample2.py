# Intentional linting issues for testing

import os


vARIABLE_TWO = 2


def test_function(x, y):
    z = x + y
    print("Sum is", z)
    return z

def add_numbers(a: int, b: int) -> int:
    """Adds two numbers."""
    return a + b

def subtract(a, b):
    return a - b
