# Simple Calculator
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b

num1 = float(input("Enter first number: "))
operator = input("Enter operator (+,-,*,/): ")
num2 = float(input("Enter second number: "))

if operator == "+":
    print("Ressult:", add(num1, num2))
elif operator ==  "-":
    print("Result:", subtract(num1, num2))
elif operator == "*":
    print("Result:", multiply(num1, num2))
elif operator == "/":
    if num2 != 0:
        print("Result:", divide(num1,num2))
    else:
        print("Can't divide by zero.")
else:
    print("Invalid operator")
    






    