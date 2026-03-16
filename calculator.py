def add(x, y):
    """Adds two numbers."""
    return x + y

def subtract(x, y):
    """Subtracts two numbers."""
    return x - y

def multiply(x, y):
    """Multiplies two numbers."""
    return x * y

def divide(x, y):
    """Divides two numbers, handling division by zero."""
    if y == 0:
        return "Error: Division by zero is not allowed."
    return x / y

def power(x, y):
    """Calculates x raised to the power y."""
    return x ** y

def main():
    print("Welcome to the Simple Calculator!")
    print("Select an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Exit")

    while True:
        choice = input("\nEnter choice (1/2/3/4/5/6): ")

        if choice == '6':
            print("Exiting the calculator. Goodbye!")
            break

        if choice in ('1', '2', '3', '4', '5'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter numerical values.")
                continue

            if choice == '1':
                print(f"Result: {num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                result = divide(num1, num2)
                print(f"Result: {num1} / {num2} = {result}")
            elif choice == '5':
                print(f"Result: {num1} ^ {num2} = {power(num1, num2)}")
        else:
            print("Invalid input. Please choose a valid operation.")

if __name__ == "__main__":
    main()
