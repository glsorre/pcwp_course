for letter in 'Python':
    if letter == 'y':
        continue
    if letter == 'o':
        break
    print(letter)

for i in range(5, 10):
    print(i)

lis = [10, 11, 12, 13, 14]
lis2 = [20, 21, 22, 23, 24]
dic = {'chiave': "valore", "key": "value"}

for i in reversed(lis):
    print(i)

for i, value in enumerate(lis):
    print(i, value)

for key, value in dic.items():
    print(key, value)

for i, j in zip(lis, lis2):
    print(i, j)

lis3 = [x**2 for x in lis if x % 2 == 0]
print(lis3)

lis4 = [(x**2, y**2) for x in lis for y in lis2 if x % 2 == 0 if y % 2 == 0]
print(lis4)


def fun(arg, karg=0, *args, **kwargs):
    print(arg)
    print(karg)
    print(*args)
    for key, value in kwargs.items():
        print(key, value)
    return arg, karg


value, second = fun("argument")
print(value, second)

value, second = fun("argument", "karg", "casa", "appartamento", animale1="cane", animale2="gatto")
print(value, second)


def myfunc(n):
    return lambda a: a * n


mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))


def this_fails():
    return 1/0

try:
    this_fails()
except ZeroDivisionError as err:
    print('Handling run-time error:', err)

# this_fails()

try:
    raise NameError('HiThere')
except NameError:
    print('An exception flew by!')

fun = lambda x: x**3

lis5 = list(map(fun, lis))
print(lis5)

lis6 = list(filter(lambda x: x % 2, lis))
print(lis5)

from functools import partial
def fun2(a, b, c):
    print(b**2 + (4 * a * c))
fun3 = partial(fun2, 5, 5)
fun3(5)
