# simple calculator

operation = input("Enter operation (+, - ,/, *): ")
num_one = int(input("Enter first number: "))
num_two = int(input("Enter second number: "))

def calculator(num_one, num_two, operation):
    if operation == "+":
        return num_one + num_two
    elif operation == "-":
        return num_one - num_two
    elif operation == "*":
        return num_one * num_two
    elif operation == "/":
        return num_one / num_two if num_two != 0 else "undefined (cannot divide by zero)"
    else:
        return "Invalid operation"

result = calculator(num_one, num_two, operation)

print(f"The result is: {result}")