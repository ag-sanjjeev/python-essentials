# method overloading
class student:
    def __init__(self):
        pass

    def avg(self, m1=None, m2=None, m3=None):
        a = 0
        if m1 is not None and m2 is not None and m3 is not None:
            a = m1 + m2 + m3
            return a
        elif m1 is not None and m2 is not None:
            a = m1 + m2
            return a


s1 = student()
print(s1.avg(1, 2, 3))
print(s1.avg(20, 30))