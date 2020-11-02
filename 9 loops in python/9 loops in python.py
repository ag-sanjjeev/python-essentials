# for and while loops available in python
# iterate with str
for x in "Hello World":
    print(x)

# iterate with list
for x in ['a', 'b', 'c']:
    print(x)

# iterate with range
for x in range(5):
    print(x)

# iterate with range starting element and ending element
for x in range(1, 5):
    print(x)

# iterate with range starting element and ending element with step value
for x in range(1, 10, 2):  # prints even element because 2 steps
    print(x)

# for else in python
# for loop was break or nothing iterate means it will execute else block
# performance wise use break statement
names = ["San", "Gan"]
for name in names:
    if name.startswith("s"):
        print("Found")
        break
else:
    print("Not Found")

# while loop in python similar as for loop
inp = 0
password = 123
while inp != password:
    inp = int(input("Password: "))
else:
    pass

