import math

# Temprature conversion Functions
def celsius_to_fahrenheit(celsius):
    return ( celsius * 9 / 5 ) + 32
def fahrenheit_to_celsius(fahrenheit):
    return ( fahrenheit - 32 ) * 5 / 9

# Area Calculation Function 
def Area(radius):
    return math.pi * radius ** 2
def Rectangle(length, width):
    return length * width

print("Temprature Conversions:")
print("25°C =", celsius_to_fahrenheit(25),"°F")
print("100°F =", fahrenheit_to_celsius(100), "°C")

print("\nArea Calculation:")
print("Area of Circle = ", Area(5))
print("Area of Rectangle = ", Rectangle(5, 7))