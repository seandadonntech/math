def add(x, y):
    return x + y

def multiply(x, y):
    return x * y  

x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
ops = input("Which operation would you like to do (add/multiply)? ")

if ops == "add":
    solution = add(x, y)
    print("Result of addition:", solution)
elif ops == "multiply":
    solution = multiply(x, y)
    print("Result of multiplication:", solution)
else:
    print("Invalid operation selected.")
