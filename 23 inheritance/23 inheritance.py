# inheritance # 1 single level inheritance
class A:
    def property(self):
        print('property 1 from A')


class B(A):  # inheritance B(A) that is A is inherited to B A - super class B - sub class
    def property2(self):
        print('property 2 from B')


a1 = A()
b1 = B()

a1.property()
b1.property()
b1.property2()


# multilevel inheritance
class C(B):
    def property3(self):
        print('property 3 from C')


c1 = C()
c1.property3()
c1.property()
c1.property2()


# multiple inheritance
class D:
    def property4(self):
        print('property 4 from D')


class E(A, D):
    def property5(self):
        print('property 5 from E')


e1 = E()
e1.property5()
e1.property4()
e1.property()


# constructor inheritance

class First:
    def __init__(self):
        print('Constructor 1')


class Second(First):
    def __init__(self):
        print('Constructor 2')
        super().__init__()  # super keyword to inherit constructor
        # because only one init executes enough though inheritance
        # if you want both class init to execute using super keyword to call it


s = Second()


# MRO Method Resolution Order In case, multiple inheritance
# it will execute left most class that we have mention
class X:
    def __init__(self):
        print('From X')

    def show(self):
        print('Hello X')


class Y:
    def __init__(self):
        print('From Y')

    def show(self):
        print('Hello Y')


class Z(Y, X):
    def __init__(self):
        print('From Z')
        super().__init__()  # it will call init from Y because we mention Y as first class
        super().show()  # same as function call

    def show(self):
        print('Hello Z')


obj = Z()