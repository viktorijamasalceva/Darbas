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
test



#Nastia
print("Available operations: add, subtract, multiply, divide")
a = input("Enter first number: ")  
b = input("Enter second number: ") 
operation = input("Enter operation: ")

result = calculate(operation, a, b)  
print(f"The result is: {result}")














