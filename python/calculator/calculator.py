# CLI Calculator
# Refactored to handle invalid inputs, such as non-numeric input
# or invalid operator input.


def calculate(num1, num2, operator):
    # Dictionary to map operators to their corresponding operations
    operators = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y,
    }
    op = operators.get(operator)
    if op:
        return op(num1, num2)
    else:
        return "Invalid Operator"


def main():
    # Try-except block to handle ValueError in case of invalid input
    while True:
        try:
            num1 = float(input("Enter first number: "))
            operator = input("Enter operator: ")
            num2 = float(input("Enter second number: "))
            result = calculate(num1, num2, operator)
            if isinstance(result, str):
                print(result)
            else:
                print(num1, operator, num2, "=", result)
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")


if __name__ == "__main__":
    main()
