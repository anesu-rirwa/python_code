# Python Calculator


def calculate():
    # Get user input
    operator = input("Enter operator (+, -, *, /): ")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter the second number: "))
    
    if operator == '+':
        return round(num1 + num2, 2)
    elif operator == '-':
        return round(num1 - num2, 2)
    elif operator == '*':
        return round(num1 * num2, 2)
    elif operator == '/':
        if num2 == 0:
            return "Error! Division by zero."
        else:
            return round(num1 / num2, 2)
    else:
        return f"Operator input {operator} is invalid."

result = calculate()
print(result)
