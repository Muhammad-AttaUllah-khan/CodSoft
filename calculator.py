def input_numbers():
    x = float(input("Enter 1st Number: "))
    y = float(input("Enter 2nd Number: "))
    return x, y

def add(x, y):
    result = x + y
    print(f"Result: {result}")

def subtract(x, y):
    result = x - y
    print(f"Result: {result}")

def multiply(x, y):
    result = x * y
    print(f"Result: {result}")

def divide(x, y):
    if y != 0:
        result = x / y
        print(f"Result: {result}")
    else:
        print("Division by zero is not allowed.")

def welcome_message():
    print("""
        1 --> Addition
        2 --> Subtraction
        3 --> Multiplication
        4 --> Division
        5 --> Exit
    """)

print("\t\t☆*: .｡. o(≧▽≦)o .｡.:*☆ Welcome To ARITHMETIC OPERATION CALCULATOR ☆*: .｡. o(≧▽≦)o .｡.:*☆ ")

while True:
    welcome_message()
    choice = int(input("Enter your choice number: "))
    
    if choice == 1:
        x, y = input_numbers()
        add(x, y)
    elif choice == 2:
        x, y = input_numbers()
        subtract(x, y)
    elif choice == 3:
        x, y = input_numbers()
        multiply(x, y)
    elif choice == 4:
        x, y = input_numbers()
        divide(x, y)
    elif choice == 5:
        break
    else:
        print("Enter a valid choice")
