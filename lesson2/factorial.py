from math import factorial

def factorial_for(n):
    if n == 0:
        return 1

    result = 1

    for i in range(1, n+1):
        result *= i

    return result

def factorial_recur(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n-1)    

assert(factorial(0) == factorial_for(0))
assert(factorial(1) == factorial_for(1))
assert(factorial(5) == factorial_for(5))
assert(factorial(1000) == factorial_for(1000))

assert(factorial(0) == factorial_recur(0))
assert(factorial(1) == factorial_recur(1))
assert(factorial(5) == factorial_recur(5))
assert(factorial(1000) == factorial_recur(1000))