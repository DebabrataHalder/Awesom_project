def get_inputs():
    try:
        num1 = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /): ").strip()
        num2 = float(input("Enter second number: "))
        return num1, operator, num2
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return None, None, None
