tasks = []
while True:
    print("\nOptions:")
    print("1. Display to-do list")
    print("2. Add a task")
    print("3. Mark a task as completed")
    print("4. Remove a task")
    print("5. Quit")
    choice = input("Enter your choice: ")
    if choice == "1":
        if not tasks:
            print("Your to-do list is empty.")
        else:
            print("To-Do List:")
            for i, task in enumerate(tasks, 1):
                status = "Done" if task["done"] else "Not Done"
                print(f"{i}. {task['name']} ({status})")
    elif choice == "2":
        task = input("Enter the task: ")
        tasks.append({"name": task, "done": False})
        print(f"Task '{task}' added to your to-do list.")
    elif choice == "3":
        if not tasks:
            print("Your to-do list is empty.")
        else:
            print("To-Do List:")
            for i, task in enumerate(tasks, 1):
                status = "Done" if task["done"] else "Not Done"
                print(f"{i}. {task['name']} ({status})")
            try:
                task_num = int(input("Enter the task number to mark as completed: ")) - 1
                if 0 <= task_num < len(tasks):
                    tasks[task_num]["done"] = True
                    print(f"Task {task_num + 1} marked as completed.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")
    elif choice == "4":
        if not tasks:
            print("Your to-do list is empty.")
        else:
            print("To-Do List:")
            for i, task in enumerate(tasks, 1):
                status = "Done" if task["done"] else "Not Done"
                print(f"{i}. {task['name']} ({status})")
            try:
                task_num = int(input("Enter the task number to remove: ")) - 1
                if 0 <= task_num < len(tasks):
                    removed_task = tasks.pop(task_num)
                    print(f"Task '{removed_task['name']}' removed from your to-do list.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")