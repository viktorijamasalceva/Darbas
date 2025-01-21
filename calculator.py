#Vika
def add(a, b):
    return a + b 

def subtract(a, b):
    return a - b 

def multiply(a, b):
    return a * b  

def divide(a, b):
    if b == 0:
        return "error"  
    return a / b
#Artur
def calculate(operation, a, b):
    if operation == "add":
        return add(a, b)
    if operation == "subtract":
        return subtract(a, b)  
    if operation == "multiply":
        return multiply(a, b)
    if operation == "divide":
        return divide(a, b)  
    else:
        raise ValueError("Error: Unknown operation")

def get_number_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Error: Invalid input, please enter a valid number")  
#Nastia


print("Available operations: add, subtract, multiply, divide")
a = get_number_input("Enter first number: ")  
b = get_number_input("Enter second number: ") 
operation = input("Enter operation: ")

try:
	result = calculate(operation, a, b)
	print(f"The result is: {result}")
except ValueError as e:
	print(e)


# test

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: Division by zero" 
    return a / b


def calculate(operation, a, b):
    if operation == "add":
        return add(a, b)
    if operation == "subtract":
        return subtract(a, b)
    if operation == "multiply":
        return multiply(a, b)
    if operation == "divide":
        return divide(a, b)
    else:
        raise ValueError("Error: Unknown operation")


def get_number_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Error: Invalid input, please enter a valid number")


print("Available operations: add, subtract, multiply, divide")

a = get_number_input("Enter first number: ")
b = get_number_input("Enter second number: ")

operation = input("Enter operation: ").lower() 

try:
    result = calculate(operation, a, b)
    print(f"The result is: {result}")
except ValueError as e:
    print(e)












