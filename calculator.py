#bad smell because of repetitive number checking. make a number checking function instead
def addition(num1, num2):
    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        print("Error: Invalid input. Please enter numeric values.")
        return '0'
    return num1 + num2


def subtraction(num1, num2):
    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        print("Error: Invalid input. Please enter numeric values.")
        return '0'
    return num1 - num2


def multiplication(num1, num2):
    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        print("Error: Invalid input. Please enter numeric values.")
        return '0'
    return num1 * num2


def division(num1, num2):
    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        print("Error: Invalid input. Please enter numeric values.")
        return  '0'
    
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
        return '0'
    
    return num1 / num2


#bad smell because of repetitive code. make a function to take in num1 and num2 instead
def option(choice):
    if choice == '1':
        num1 = input("Enter first number: ")
        num2 = input("Enter second number: ")
        result = addition(num1, num2)
        if result == '0':
            return
        print("The result of addition is: " + str(result))
        return result
    
    elif choice == '2':
        num1 = input("Enter first number: ")
        num2 = input("Enter second number: ")
        result = subtraction(num1, num2)
        if result == '0':
            return
        print("The result of subtraction is: " + str(result))
        return result
    
    elif choice == '3':
        num1 = input("Enter first number: ")
        num2 = input("Enter second number: ")
        result = multiplication(num1, num2)
        if result == '0':
            return
        print("The result of multiplication is: " + str(result))
        return result
    
    elif choice == '4':
        num1 = input("Enter first number: ")
        num2 = input("Enter second number: ")
        result = division(num1, num2)
        if result == '0':
            return
        print("The result of division is: " + str(result))
        return result
    
    else:
        print("Error: Invalid choice. Please try again.")
        return
    

def main():
    #bad smell of repetitive print statements
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