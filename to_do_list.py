import os
from datetime import date

def custom_welcome_msg(name):
    print(f""" **WELCOME {name}'s TO-DO LIST APPLICATION**
        1 --> Add Task
        2 --> View Tasks
        3 --> Delete list
        4 --> Exit
    """)

def create_todo_list(name):
    """Create a text file with the user's name as the filename and display a message."""
    with open(f"{name}.txt", 'a') as f:
        f.write("")
    print(f"{name}'s To-Do List has been created successfully.")

def add_task(name):
    """Add a task to the user's to-do list."""
    task = input("Enter Task to Add: ")
    with open(f"{name}.txt", 'a') as f:
        f.write(f"{task} - {date.today()}\n")

def remove_task(name):
    """Remove a task from the user's to-do list."""
    task = input("Enter Task to Remove: ")
    try:
        new_list = ""
        with open(f"{name}.txt", 'r') as f:
            lines = f.readlines()
            for line in lines:
                if task not in line:
                    new_list += line
        with open(f"{name}.txt", 'w') as f:
            f.write(new_list)
        print(f"Task '{task}' has been removed.")
    except:
        print("Oops, something went wrong. Cannot remove this task.")

def delete_todo_list(name):
    """Delete the user's to-do list file."""
    try:
        os.remove(f"{name}.txt")
        print(f"{name}'s to-do list has been deleted successfully.")
    except:
        print("Oops, something went wrong. Cannot delete the list file.")

def view_tasks(name):
    """View the tasks in the user's to-do list."""
    try:
        with open(f"{name}.txt", 'r') as f:
            result = f.read()
            if result == "":
                print(f"{name}'s To-Do List is empty.")
            else:
                print(f"{name}'s To-Do List:\n{result}")
    except FileNotFoundError:
        print(f"{name}'s To-Do List not found. Please create a list first.")

name = input("Please enter your name: ")
create_todo_list(name)

while True:
    custom_welcome_msg(name)
    choice = int(input("Enter choice: "))
    if choice == 1:
        add_task(name)
    elif choice == 2:
        view_tasks(name)
    elif choice == 3:
        delete_todo_list(name)
        break
    elif choice == 4:
        exit
    else:
        print("Invalid choice")
