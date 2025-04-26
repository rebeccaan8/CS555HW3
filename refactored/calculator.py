
def validate_numbers(num1, num2):
    """Helper function to validate and convert input strings to numbers."""
    try:
        num1 = float(num1)
        num2 = float(num2)
        return True, num1, num2
    except ValueError:
        print("Error: Invalid input. Please enter numeric values.")
        return False, 0, 0


def addition(num1, num2):
    is_valid, n1, n2 = validate_numbers(num1, num2)
    if not is_valid:
        return '0'
    return n1 + n2


def subtraction(num1, num2):
    is_valid, n1, n2 = validate_numbers(num1, num2)
    if not is_valid:
        return '0'
    return n1 - n2


def multiplication(num1, num2):
    is_valid, n1, n2 = validate_numbers(num1, num2)
    if not is_valid:
        return '0'
    return n1 * n2


def division(num1, num2):
    is_valid, n1, n2 = validate_numbers(num1, num2)
    if not is_valid:
        return '0'

    if n2 == 0:
        print("Error: Division by zero is not allowed.")
        return '0'

    return n1 / n2


def get_numbers():
    """Get two numbers from user input."""
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    return num1, num2


def option(choice):
    # Dictionary mapping choices to operation functions and their descriptions
    operations = {
        '1': (addition, "addition"),
        '2': (subtraction, "subtraction"),
        '3': (multiplication, "multiplication"),
        '4': (division, "division")
    }

    if choice not in operations:
        print("Error: Invalid choice. Please try again.")
        return '0'

    operation_func, operation_name = operations[choice]

    # Get numbers from user
    num1, num2 = get_numbers()

    # Perform the selected operation
    result = operation_func(num1, num2)

    # If result is '0', there was an error
    if result == '0':
        return

    print(f"The result of {operation_name} is: {result}")
    return result


def main():
    print("What would you like to do?")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Enter your choice (1-4): ")
    answer = option(choice)
    return answer


if __name__ == "__main__":
    main()