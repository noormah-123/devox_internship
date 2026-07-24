# Day 5 - Python OOP: Inheritance

## Task

Create three classes demonstrating inheritance:

* `Shape` as the parent class
* `Circle` as a child class
* `Rectangle` as a child class

Each child class should have its own `area()` method to calculate the area of the shape.

## Code

```python
# Parent class
class Shape:
    def Area(self):
        print("Area Calculation")


# Child class 1
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def Area(self):
        return 3.14 * self.radius ** 2


# Child class 2
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def Area(self):
        return self.length * self.width


# Objects
obj_circle = Circle(5)
obj_Rectangle = Rectangle(5, 4)

print("Circle Area:", obj_circle.Area())
print("Rectangle Area:", obj_Rectangle.Area())
```

## Output

```text
Circle Area: 78.5
Rectangle Area: 20
```

## Concepts Learned

* Classes and Objects
* Inheritance
* Parent Class
* Child Classes
* Constructors (`__init__`)
* Method Overriding
* Polymorphism
* `self` keyword

## Learning

In this task, I learned how inheritance works in Python. The `Shape` class is the parent class, while `Circle` and `Rectangle` are child classes that inherit from it.

Both child classes have their own `area()` method. The `Circle` class calculates the area using the circle formula, while the `Rectangle` class calculates the area using length multiplied by width.

This task also demonstrated method overriding because both child classes define their own version of the `area()` method.

## Folder Structure

```text
Day_3/
│
├── task.py
└── README.md
```
