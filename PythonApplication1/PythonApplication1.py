tasks = []

while True:
    print("\nTo-Do List")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added!")
    elif choice == "2":
        print("Your tasks:")
        for i, t in enumerate(tasks, start=1):
            print(f"{i}. {t}")
    elif choice == "3":
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            tasks.pop(num-1)
            print("Task deleted!")
        else:
            print("Invalid number!")
    elif choice == "4":
        break
    else:
        print("Invalid choice, try again!")
