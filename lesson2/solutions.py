def arithtmetic(a, b):
    return {
        "sum": a + b,
        "product": a * b,
        "division": a / b,
        "remainder": a % b
    }

def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n-1)

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