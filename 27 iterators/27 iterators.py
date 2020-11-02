# iterators used to iterate elements inside the variable
a = [1, 2, 3, 4]
print(a[1])

for i in a:
    print(i, end="")

print()
# iterator prints each elements without indexing
i = iter(a)
# __next__ and next() are same
print(i.__next__())
print(next(i))


# own even iterator function

class evens:
    def __init__(self):
        self.num = 0

    def __iter__(self):
        return self

    def __next__(self):
        val = self.num
        self.num += 2
        return val


e = evens()
print(e.__next__())
print(e.__next__())

print(next(e))
for i in e:
    print(i)  # this will print but wont stop because no termination
    if i > 20:
        break
