import random
import string

def generate_password(level, length):
    if level == "simple":
        characters = string.ascii_letters + string.digits
    elif level == "medium":
        characters = string.ascii_letters + string.digits + '#$%'
    elif level == "tough":
        characters = string.ascii_letters + string.digits + '!~@#$%^&*(_+|?><|)'
    else:
        return "Invalid Choice"
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

print("\t\t☆*: .｡. o(≧▽≦)o .｡.:*☆ Welcome To RANDOM PASSWORD GENERATOR ☆*: .｡. o(≧▽≦)o .｡.:*☆ \n")

try:        
    length = int(input("Enter desired length of Password (min=4, max=16): "))
    while length not in range(4, 17):
        print("Length not suitable.\n")
        length = int(input("Enter length again: "))
except ValueError:
    print("Invalid Input.\nExiting.......")
    exit()

valid_levels = ['simple', 'medium', 'tough']
level = input("Enter Complexity level ('simple', 'medium', 'tough'): ").lower()
while level not in valid_levels:
    print("Invalid Input")
    level = input("Enter Complexity level ('simple', 'medium', 'tough'): ").lower()

password = generate_password(level, length)
print(f"Password Generated is: {password}")
print("Thanks for Using!!\nExiting...")
