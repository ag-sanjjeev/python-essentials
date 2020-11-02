# functions in python
def add1(a, b):
    return a + b


sum1 = add1(1, 3)  # add two line spaces after function end
print(sum1)


def add2(a: int, b: int) -> int:  # tells return type and parameters type
    return a + b


sum2 = add2(2, 4)
print(sum2)


def add3(a: float, b: float) -> float:
    return a + b


sum3 = add3(2, b=3)  # keyword argument
print(sum3)


def add4(a, b: int = 2) -> tuple:  # default argument
    return a, a + b


sum4 = add4(1)
print(sum4)


# *args in python


def multiply(*list):
    total = 1
    for number in list:
        total *= number
    return total


print(multiply([1, 2, 3, 4]))
print(multiply(1, 2, 3, 4))  # takes tuple as list but not list as list


# **args in python


def user_details(**user):
    print(user)  # it will print as dictionary or JSON format
    print(user['id'])
    print(user['Name'])


user_details(id=1, Name="San", Role="Developer")  # keyword argument
