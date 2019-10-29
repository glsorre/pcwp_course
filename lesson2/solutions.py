def arithtmetic(a, b):
    return {
        "sum": a + b,
        "multiplication": a * b,
        "division": a / b,
        "modulus": a % b
    }

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

from math import factorial

def memoize(fun):
    cache = {}

    def memoized(*args):
        if args in cache:
            return cache[args]
        else:
            result = fun(*args)
            cache[args] = result
            return result

    return memoized