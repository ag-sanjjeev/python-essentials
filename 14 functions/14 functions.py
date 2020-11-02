# functions
def greet():  # function definition
    print('Hello World')


greet()  # explicit function call


# function type2
def add(a, b):
    return a + b


print(add(1, 2))


# function type3
def mul(a, b):
    c = a * b
    print(c)


mul(3, 2)


# function type3 returning multiple values
def arith(x, y):
    a = x + y
    b = x - y
    c = x * y
    d = x / y
    e = x // y
    f = x % y
    g = x ** y
    return a, b, c, d, e, f, g


a, b, c, d, e, f, g = arith(5, 2)
print(a, b, c, d, e, f, g)