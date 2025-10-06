# Intentional linting issues for testing

import os, sys

# Function with spacing and naming issues
def testFunction( x, y ):
  z= x+y
  print("Sum is",z)
  return z

# Unused variable
unused_var = 42

# Bad indentation
if True:
  print("This line is fine")
   print("This line has bad indentation")

# Long line for Black to flag
long_line = "This is a very long line that will exceed the 88 character limit that Black enforces in default configuration"

# Correct function for comparison
def add_numbers(a: int, b: int) -> int:
    """Adds two numbers."""
    return a + b

# Missing docstring
def subtract(a,b):
    return a-b

