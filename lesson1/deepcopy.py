xs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
ys = xs.copy()

print(xs)
print(ys)

xs.append(['new sublist'])

print(xs)
print(ys)

xs[1][0] = 'X'

print(xs)
print(ys)

from copy import deepcopy

xs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
ys = deepcopy(xs)

print(xs)
print(ys)

xs.append(['new sublist'])

print(xs)
print(ys)

xs[1][0] = 'X'

print(xs)
print(ys)