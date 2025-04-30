from src.input import get_inputs

def main():
    num1, operator, num2 = get_inputs()

    if num1 is None or operator is None or num2 is None:
        return

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 == 0:
            print("Error: Division by zero is undefined.")
            return
        result = num1 / num2
    else:
        print("Invalid operator. Please use +, -, *, or /.")
        return

    print(f"Result: {result}")

if __name__ == "__main__":
    main()

