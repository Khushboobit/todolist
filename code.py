def display_tasks(tasks):
    if not tasks:
        print("No tasks in the list.")
    else:
        for i, task in enumerate(tasks):
            status = "Done" if task['completed'] else "Pending"
            print(f"{i+1}. {task['task']} - {status}")

def add_task(tasks):
    task = input("Enter the task: ")
    tasks.append({"task": task, "completed": False})
    print("Task added successfully.")

def complete_task(tasks):
    display_tasks(tasks)
    task_num = int(input("Enter the task number to mark as completed: ")) - 1
    if 0 <= task_num < len(tasks):
        tasks[task_num]['completed'] = True
        print("Task marked as completed.")
    else:
        print("Invalid task number.")

def delete_task(tasks):
    display_tasks(tasks)
    task_num = int(input("Enter the task number to delete: ")) - 1
    if 0 <= task_num < len(tasks):
        tasks.pop(task_num)
        print("Task deleted successfully.")
    else:
        print("Invalid task number.")

def main():
    tasks = []
    while True:
        print("\nTo-Do List Manager")
        print("1. View tasks")
        print("2. Add task")
        print("3. Mark task as completed")
        print("4. Delete task")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            complete_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()