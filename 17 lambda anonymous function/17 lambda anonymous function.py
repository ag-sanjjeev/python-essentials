# lambda is anonymous function for use function without define and doest not use anymore
f = lambda a, b: a * b

print(f(3, 4))

# use of lambda
# filter

num = [1, 2, 3, 4, 5, 6, 7, 8, 9]

even_num = list(filter(lambda a: a % 2 == 0, num))
print(even_num)

# map
squares = list(map(lambda a: a * a, num))
print(squares)

# reduce

from functools import reduce

sums = reduce(lambda a, b: a + b, num)
print(sums)
