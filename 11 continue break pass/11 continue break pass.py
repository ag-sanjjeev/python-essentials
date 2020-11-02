# continue and continue to the next statements
for i in range(5):

    if i == 2:
        print('Hello ', i)
    continue

# break and break the statement flow go to the next statement
for i in range(5):
    print('Hello ', i)
    if i == 3:
        break

# pass and pass for empty block such as if, elif, for, while, function
if i == 3:
    pass
