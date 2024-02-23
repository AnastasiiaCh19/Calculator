import sys

def add(num1, num2: float) -> float:
    return num1 + num2

def subtract(num1, num2: float) -> float:
    return num1 - num2

def multiplication(num1, num2: float) -> float:
    return num1 * num2

def devision(num1, num2: float) -> float:
    return num1 / num2

def main():
    print("Calculator")

    while True:
        print("Options:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiplication")
        print("4. Division")
        print("5. Quit")

        choice = (input("Please enter your choice 1/2/3/4/5: ")).strip

        if choice == '1':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            result = add(num1, num2)
            print("Result: ", result)
        elif choice == '2':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            result = subtract(num1, num2)
            print("Result: ", result)
        elif choice == '3':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            result = multiplication(num1, num2)
            print("Result: ", result)
        elif choice == '4':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            result = devision(num1, num2)
            print("Result: ", result)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, 4 or 5.")

if __name__ == "__main__":
    main()