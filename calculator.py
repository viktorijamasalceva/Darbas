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
	if operation == "substract":
		return substract(a, b)
	if operation == "multiply":
		return multiply(a, b)
	else:
		raise ValueError("error")

def get_input(prompt):
	while True:
		try:
			return float(input(prompt))
		exept ValueError:
			print(error)



#Nastia
print("Available operations: add, subtract, multiply, divide")
a = input("Enter first number: ")  
b = input("Enter second number: ") 
operation = input("Enter operation: ")

result = calculate(operation, a, b)  
print(f"The result is: {result}")














