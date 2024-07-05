def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y

def square_root(x):
    if x < 0:
        raise ValueError("Cannot calculate square root of a negative number!")
    return x ** 0.5

def exponentiation(x, y):
    return x ** y

def calculator():
    print("Welcome to Simple Calculator!")
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Square Root")
    print("6. Exponentiation")
    print("0. Exit")

    while True:
        choice = input("Enter choice (0-6): ")

        if choice in ['0', '1', '2', '3', '4', '5', '6']:
            if choice == '0':
                print("Exiting...")
                break
            
            try:
                if choice in ['1', '2', '3', '4', '6']:
                    num1 = float(input("Enter first number: "))
                    num2 = float(input("Enter second number: "))

                    if choice == '1':
                        print("Result:", add(num1, num2))
                    elif choice == '2':
                        print("Result:", subtract(num1, num2))
                    elif choice == '3':
                        print("Result:", multiply(num1, num2))
                    elif choice == '4':
                        print("Result:", divide(num1, num2))
                    elif choice == '6':
                        print("Result:", exponentiation(num1, num2))
                
                elif choice == '5':
                    num = float(input("Enter a number: "))
                    print("Result:", square_root(num))

            except ValueError as e:
                print("Error:", e)
        else:
            print("Invalid input. Please enter a number between 0 and 6.")

if __name__ == "__main__":
    calculator()
