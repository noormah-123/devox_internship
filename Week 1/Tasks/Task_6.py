# List to store tasks
tasks = []

# Function to add a task
def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added successfully.")

# Function to remove a task
def remove_task(task_number):
    try:
        removed = tasks.pop(task_number - 1)
        print(f"Task '{removed}' removed successfully.")
    except IndexError:
        print("Error: Invalid task number.")

# Function to view tasks
def view_tasks():
    if not tasks:
        print("No tasks in the list.")
    else:
        print("\nTo-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
    print()

# Simple menu-driven program
def main():
    while True:
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            task = input("Enter task: ")
            add_task(task)

        elif choice == '2':
            view_tasks()
            try:
                num = int(input("Enter task number to remove: "))
                remove_task(num)
            except ValueError:
                print("Error: Please enter a valid number.")

        elif choice == '3':
            view_tasks()

        elif choice == '4':
            print("Exiting To-Do List. Goodbye!")
            break

        else:
            print("Invalid choice. Please select 1-4.")

# Run the app
main()