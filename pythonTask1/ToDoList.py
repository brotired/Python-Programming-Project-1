# To Do List Program

tasks = []

while True:
    print("\nTo Do List")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Enter a new task: ")
        tasks.append(task)
        print("Task added!")

    elif choice == "2":
        print("\nYour Tasks:")

        if len(tasks) == 0:
            print("No tasks yet.")
        else:
            for task in tasks:
                print("- " + task)

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")