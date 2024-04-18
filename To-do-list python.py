import json
from datetime import datetime


TASKS_FILE = "tasks.json"

def load_tasks():
    try:
        with open(TASKS_FILE, 'r') as file:
            tasks = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        tasks = []
    return tasks

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=2)

def display_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return

    print("ID | Description | Due Date | Status")
    print("-" * 40)
    for task in tasks:
        print(f"{task['id']} | {task['description']} | {task['due_date']} | {task['status']}")

def add_task(description, due_date):
    tasks = load_tasks()
    task_id = len(tasks) + 1
    new_task = {
        'id': task_id,
        'description': description,
        'due_date': due_date,
        'status': 'Incomplete'
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print("Task added successfully.")

def mark_complete(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = 'Complete'
            save_tasks(tasks)
            print(f"Task {task_id} marked as complete.")
            return
    print(f"Task {task_id} not found.")

def remove_task(task_id):
    tasks = load_tasks()
    tasks = [task for task in tasks if task['id'] != task_id]
    save_tasks(tasks)
    print(f"Task {task_id} removed.")

def main():
    while True:
        print("\n1. Display Tasks")
        print("2. Add Task")
        print("3. Mark Task as Complete")
        print("4. Remove Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            tasks = load_tasks()
            display_tasks(tasks)
        elif choice == '2':
            description = input("Enter task description: ")
            due_date = input("Enter due date (optional, format: YYYY-MM-DD): ")
            add_task(description, due_date)
        elif choice == '3':
            task_id = int(input("Enter task ID to mark as complete: "))
            mark_complete(task_id)
        elif choice == '4':
            task_id = int(input("Enter task ID to remove: "))
            remove_task(task_id)
        elif choice == '5':
            print("Exiting the To-Do List application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
