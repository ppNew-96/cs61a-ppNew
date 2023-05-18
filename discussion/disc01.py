# Control: direct the flow of a program using logical statements.

# if-elif-else allows a program to skip sections of code.

# boolean operators:
# 1. not always returns True or False, not None is also True.
# 2. and operator evaluates expressions in order and stop evaluating once it reaches the first false value,
#    otherwise it returns the last value.
# 3. or operator returns the first true value, otherwise it returns the last value.

# Questions:

# Alfonso will only wear a jacket outside if it is below 60 degrees or it is raining.
# Write a function that takes in the current temperature and a boolean value telling
# if it is raining and returns True if Alfonso will wear a jacket and False otherwise.
def wears_jacket_with_if(temp, raining):
    """
    >>> wears_jacket_with_if(90, False)
    False
    >>> wears_jacket_with_if(40, False)
    True
    >>> wears_jacket_with_if(100, True)
    True
    """
    return False if temp >= 60 and not raining else True


# Write a function that returns True if a positive integer n is a prime number and False otherwise.
import math


def is_prime(n):
    divisor = 2
    threshold = int(math.sqrt(n))
    while divisor <= threshold:
        if n % divisor == 0:
            return False
        divisor += 1
    return True