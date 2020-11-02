# error handling
# handle error when arise that not stop your program execution
# errors three type compile time error, run time error, logical error
# error arise from critical statements
a = 5
b = 0

print(a)  # this is normal statement
try:
    print(a/b)  # this is critical statement and cause an error
except Exception as e:  # e is exception object
    print("Error : ", e)

print("Program executes")

# another way of error handling model
a, b = 0, 0

try:
    a = int(input("Enter a numbers"))
    b = int(input("Enter b numbers"))
    print(a/b)
except ZeroDivisionError as e:
    print("Divided by zero not possible", e)
except ValueError as e:
    print("Invalid input")
except Exception as e:
    print("Error : ", e)
finally:
    print("All resource and connections closing")