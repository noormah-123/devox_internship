# Parent class
class Shape:  
    def Area(self):
        print("Area Calculation")

# Child class 1
class Circle(Shape):  #Child class 
    def __init__(self, radius):
        self.radius = radius
    def Area(self):
        return 3.14 * self.radius ** 2
    
# Child class 2
class   Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def Area(self):
        return self.length * self.width

# Objects
obj_circle = Circle(5)
obj_Rectangle = Rectangle(5, 4)

print("Circle Area: ", obj_circle.Area())
print("Rectangle Area: ", obj_Rectangle.Area())

