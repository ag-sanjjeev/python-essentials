# logical and logical or logical not
name = input("Your Name : ")
if not name.strip():
    print("Name is empty")

age = 18
if age <= 18 and age >= 65:
   print("You are eligible")

if 18 >= age <= 65:  # chaining expression for conditional
    print("You are eligible")

# ternary operator
message = "Your Are Eligible" if age >= 18 else "Not Eligible"
print(message)