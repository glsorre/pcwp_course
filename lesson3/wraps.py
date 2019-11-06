from functools import wraps
from math import factorial
from timeit import timeit

def memoize_with_wraps(f):
    cache = {}

    @wraps(f)
    def memoized(*args, **kwargs):
        if args in cache:
            return cache[args]
        else:
            result = f(*args, **kwargs)
            cache[args] = result
            return result

    return memoized

def memoize_without_wraps(f):
    cache = {}

    def memoized(*args):
        if args in cache:
            return cache[args]
        else:
            result = f(*args)
            cache[args] = result
            return result

    return memoized

@memoize_with_wraps
def factorial_with(n):
    """
    this is factorial_with doc string
    """
    return factorial(n)

@memoize_without_wraps
def factorial_without(n):
    """
    this is factorial_without doc string
    """
    return factorial(n)

print(factorial_with.__name__)
print(factorial_with.__doc__)
print(factorial_without.__name__)
print(factorial_without.__doc__)
