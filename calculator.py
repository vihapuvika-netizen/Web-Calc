# A Simple Python Calculator for Beginners
# This program allows users to perform basic arithmetic operations: addition, subtraction, multiplication, and division.

def add(x, y):
    """This function adds two numbers"""
    return x + y

def subtract(x, y):
    """This function subtracts two numbers"""
    return x - y

def multiply(x, y):
    """This function multiplies two numbers"""
    return x * y

def divide(x, y):
    """This function divides two numbers"""
    if y == 0:
        return "Error! Division by zero is not allowed."
    return x / y

def calculator():
    print("====================================")
    print("    Welcome to Python Calculator!   ")
    print("====================================")
    
    while True:
        # Display menu options
        print("\nSelect operation:")
        print("1. Add (+)")
        print("2. Subtract (-)")
        print("3. Multiply (*)")
        print("4. Divide (/)")
        print("5. Exit")
        
        # Take input from the user
        choice = input("Enter choice (1/2/3/4/5): ").strip()
        
        # Check if the user wants to exit
        if choice == '5':
            print("\nThank you for using Python Calculator. Goodbye!")
            break
            
        # Check if choice is one of the valid options
        if choice in ('1', '2', '3', '4'):
            try:
                # Ask user for the numbers to calculate
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                # Handle cases where the user inputs something that isn't a number
                print("Invalid input! Please enter numbers only.")
                continue
            
            # Perform calculation based on choice
            if choice == '1':
                result = add(num1, num2)
                print(f"\nResult: {num1} + {num2} = {result}")
            elif choice == '2':
                result = subtract(num1, num2)
                print(f"\nResult: {num1} - {num2} = {result}")
            elif choice == '3':
                result = multiply(num1, num2)
                print(f"\nResult: {num1} * {num2} = {result}")
            elif choice == '4':
                result = divide(num1, num2)
                print(f"\nResult: {num1} / {num2} = {result}")
        else:
            print("Invalid choice! Please select a number from 1 to 5.")

# This condition ensures the calculator only runs if we run this script directly,
# rather than importing it as a module.
if __name__ == '__main__':
    calculator()
