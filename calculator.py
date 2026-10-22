"""Simple calculator: + - * / with a continue/exit loop."""


def read_number(prompt):
    """Keep asking until the user enters a valid number."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def calculate(num1, num2, operator):
    """Return the result, or None if the operation is invalid."""
    match operator:
        case "+":
            return num1 + num2
        case "-":
            return num1 - num2
        case "*":
            return num1 * num2
        case "/":
            if num2 == 0:
                print("Division by zero is not allowed.")
                return None
            return num1 / num2
        case _:
            print("Please choose one of the operators: + - * /")
            return None


def ask_continue():
    """Return True to continue, False to exit."""
    while True:
        choice = input("Continue = 1, Exit = 0: ").strip()
        if choice == "1":
            return True
        if choice == "0":
            return False
        print("Please enter 1 or 0.")


def main():
    while True:
        num1 = read_number("Enter the first number: ")
        num2 = read_number("Enter the second number: ")
        operator = input("Enter an operator (+ - * /): ").strip()

        result = calculate(num1, num2, operator)
        if result is not None:
            print("Result:", result)

        if not ask_continue():
            break


if __name__ == "__main__":
    main()
