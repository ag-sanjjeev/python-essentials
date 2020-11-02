# if elseif else in python
user = input("User Name: ")
password = input("Pass Word: ")

if user == 'san' and password == '123':
    print("login successfully")
elif user != 'san':
    print("User name is incorrect")
elif password != '123':
    print("Password is incorrect")
else:
    print("Nothing to do")

# empty if else or block means to use pass word to carry over next process
x = 1
if x == 1:
    pass
else:
    pass

print("All done")