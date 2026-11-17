# Personal Mini-Toolkit

print("================================")
print("Welcome to My Personal Toolkit!")
print("================================")

# Store tasks in a list
tasks = []

# Main menu loop
while True:
    print("\nPlease choose a tool:")
    print("1. Simple Calculator")
    print("2. To-Do List")
    print("3. Number Checker")
    print("4. Quit")

    choice = input("Enter your choice (1-4): ")

    # Tool 1: Simple Calculator
    if choice == "1":
        print("\nSimple Calculator")

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")

        operation = input("Choose operation (1-4): ")

        if operation == "1":
            print(f"Answer: {num1 + num2}")

        elif operation == "2":
            print(f"Answer: {num1 - num2}")

        elif operation == "3":
            print(f"Answer: {num1 * num2}")

        elif operation == "4":
            if num2 != 0:
                print(f"Answer: {num1 / num2}")
            else:
                print("Cannot divide by zero!")

        else:
            print("Invalid operation!")

    # Tool 2: To-Do List
    elif choice == "2":
        while True:
            print("\nTO-DO LIST")
            print("1. Add a task")
            print("2. View tasks")
            print("3. Return to main menu")

            task_choice = input("Choose an option: ")

            if task_choice == "1":
                task = input("Enter your task: ")
                tasks.append(task)
                print(f"Task '{task}' added successfully!")

            elif task_choice == "2":
                if len(tasks) == 0:
                    print("Your task list is empty.")
                else:
                    print("\nYour tasks:")
                    for task in tasks:
                        print(f"- {task}")

            elif task_choice == "3":
                break

            else:
                print("Invalid choice. Try again!")

    # Tool 3: Number Checker
    elif choice == "3":
        print("\nNUMBER CHECKER")

        number = float(input("Enter a number: "))

        if number > 0:
            print(f"{number} is a positive number.")

        elif number < 0:
            print(f"{number} is a negative number.")

        else:
            print("The number is zero.")

    # Quit the program
    elif choice == "4":
        print("Thank you for using my toolkit. Goodbye!")
        break

    # Handle invalid choices
    else:
        print("Invalid choice. Please select 1, 2, 3 or 4.")