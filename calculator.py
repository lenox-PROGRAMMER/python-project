# Define the calculator function to allow repeated execution
def calculator():
    # Dictionary to map user choices to operations
    operations = {
        1: "Addition",
        2: "Subtraction",
        3: "Division",
        4: "Multiplication",
        5: "Modulus"
    }

    # Display available operations
    print("\nSelect an operation:")
    for key, value in operations.items():
        print(f"{key}. {value}")

    try:
        # Get the user's choice
        option = int(input("Choose an operator (1-5): "))

        # Check if the choice is valid
        if option not in operations:
            print("Invalid choice! Please select a number between 1 and 5.")
            return calculator()  # Restart function if invalid choice

        # Get user input for numbers
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        # Handle division or modulus by zero
        if option == 3 and num2 == 0:
            print("Error: Division by zero is not allowed.")
            return calculator()
        elif option == 5 and num2 == 0:
            print("Error: Modulus by zero is not allowed.")
            return calculator()

        # Perform calculations using a dictionary lookup
        result = {
            1: num1 + num2,  # Addition
            2: num1 - num2,  # Subtraction
            3: num1 / num2,  # Division (Already checked for zero)
            4: num1 * num2,  # Multiplication
            5: num1 % num2   # Modulus (Already checked for zero)
        }[option]

        # Display the result
        print(f"\nThe result of {operations[option]} is: {result}\n")

    except ValueError:
        # Catch non-numeric input errors
        print("Invalid input! Please enter numeric values.")
        return calculator()

# Run the calculator function
calculator()
