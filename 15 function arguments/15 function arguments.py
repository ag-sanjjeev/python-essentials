# arguments in function
def add(a, b):  # formal arguments
    print(a + b)


add(1, 2)  # actual arguments


# actual arguments are 4 types
# 1. position
def employee(id, name):
    print(id, name)


employee('1', 'san')

# 2. keyword argument

employee(id='1', name='san')


# 3. default argument

def employee2(name2, id2='1'):
    print(id2, name2)


employee2('san')


# 4. variable length argument
# no of parameters to be unknown means use variable length parameter

def add(a, *b):  # b as tuples multiple parameters
    print(a, b)


add(1, 2, 3, 4, 5)


# 5. keyword length argument
# we can pass parameter with keyword index

def add1(name, **details):
    print(name);
    print(details)
    for key, val in details.items():
        print(key, val)


add1('san', id=19, position='developer', mob='123')