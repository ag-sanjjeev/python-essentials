# magic methods describes the usage in data types
# this mainly used to overwrite existing operation such as operator overloading
a = 2
b = 1
print(a + b)
print(int.__add__(a, b))  # both are same that is normal class structure
print(int.__sub__(a, b))
print(int.__mul__(a, b))
print(int.__truediv__(a, b))
a, b = 3.2, 1.4
print(float.__add__(a, b))
a, b = 'Hello', 'World'
print(str.__add__(a, b))