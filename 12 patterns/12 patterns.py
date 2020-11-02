# pattern1
# 4 row 4 column * printing

for i in range(4):
    for j in range(4):
        print('* ', end='')  # for same line print
    print()  # for new line break

# left angle triangle pattern

for i in range(4):
    for j in range(i+1):
        print('* ', end='')
    print()

# mirror left angle triangle

for i in range(4):
    for j in range(4-i):
        print('* ',end='')
    print()

