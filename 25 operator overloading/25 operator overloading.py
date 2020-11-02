# operator overloading is the concept to define functionality to existing method
# it uses magic method


class student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        # s3 = student(m1, m2)
        return m1 + m2

    def __gt__(self, other):
        m1 = self.m1 + self.m2
        m2 = other.m1 + other.m2
        return m1 > m2


s1 = student(10, 20)
s2 = student(30, 50)
s3 = s1 + s2
print(s3)

if s1 > s2:
    print("S1 has first mark")
else:
    print("S2 has first mark")