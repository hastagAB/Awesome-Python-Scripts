import json
import os
import datetime

# Define the data file to store tasks
TASKS_FILE = "tasks.json"

# Load tasks from the data file (if it exists)
tasks = []

if os.path.exists(TASKS_FILE):
    with open(TASKS_FILE, "r") as file:
        tasks = json.load(file)

def save_tasks():
    # Save tasks to the data file
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file)

def add_task():
    task_name = input("Enter the task name: ")
    due_date = input("Enter the due date (YYYY-MM-DD): ")

    try:
        due_date = datetime.datetime.strptime(due_date, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return

    tasks.append({"name": task_name, "due_date": due_date})
    save_tasks()
    print(f"Task '{task_name}' added successfully!")

def view_tasks():
    print("Tasks:")
    for idx, task in enumerate(tasks, start=1):
        print(f"{idx}. {task['name']} (Due: {task['due_date']})")

def delete_task():
    view_tasks()
    task_index = input("Enter the task number to delete: ")

    try:
        task_index = int(task_index)
        if 1 <= task_index <= len(tasks):
            deleted_task = tasks.pop(task_index - 1)
            save_tasks()
            print(f"Task '{deleted_task['name']}' deleted successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")

while True:
    print("\nTask Scheduler Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please choose a valid option.")

print("Goodbye!")
