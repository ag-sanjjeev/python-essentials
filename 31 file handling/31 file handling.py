# file handling
f = open("text data.txt", "r")  # reading file
print(f.read())  # reads entire file
print(f.readline())  # reads first line this has inbuild pointer to move arround lines when loop it
print(f.readline(5))  # reads first 5 characters

# creating a file or write file
f1 = open('text data1.txt', 'w')  # write with replace existing data
f1.write("The new data")
f1.write("The another data")  # it will replace previous data

f1 = open('text data1.txt', 'a')  # this will append data not replace
f1.write("The again new data")

# copy and write in new file
f = open("text data.txt", "r")
f1 = open("text data1.txt", "a")
# f1.write(f.read())
for data in f:
    f1.write(data)
