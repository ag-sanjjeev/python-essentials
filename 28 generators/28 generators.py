# generator is a functionality that gives iterators as a return
def evens():
    n = 0

    while n <= 20:
        yield n  # it will return as iterator
        n += 2


val = evens()
print(iter(val))
print(next(val))
print(next(val))

for i in val:
    print(val.__next__())

# ends with exception because iterators has break out of while loop
# it will be useful to handle huge number of data from a database to handle one record at a time
