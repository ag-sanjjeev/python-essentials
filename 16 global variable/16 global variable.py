# accessing global variable
a = 10  # globally accessible
b = 15
print(a)
print(b)


def values():
    global a
    a = 12
    b = 13
    print(a)
    print(b)


values()
print(a)
print(b)

# globals function get access of all global variable


def value1():
    x = globals()['a']
    print(x)
    x = globals()['a'] = 10
    print(x)


value1()