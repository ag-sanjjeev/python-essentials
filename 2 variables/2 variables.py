# variable declaration and initialization
x = 1
y = 1

a, b = 2, 3

c = d = 4
print(x)
print(y)
print(a)
print(b)
print(c)
print(d)

# mutable and immutable of variable
# int float char string bool are immutable that storage place not modified even replace values
val = 1
print(id(val))  # return memory location
val += 1
print(id(val))

# list are mutable variable location not changed
val2 = [1, 2, 3]
print(id(val2))
val2.append(4)
print(id(val2))

# formatted strings
val3 = f"{len(val2)} {2 + 3} "
print(val3)