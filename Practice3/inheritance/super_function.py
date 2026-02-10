"""
Use the super() Function
Python also has a super() function that will make the child class inherit all the methods
and properties from its parent:
"""

class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}")

class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height

    def describe(self):
        print(f"It is a triangle with an area of {self.width * self.height / 2}cmˆ2")
        super().describe()

class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width

    def describe(self):
        print(f"It is a square with an area of {self.width * self.width}cmˆ2")
        super().describe()


class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius

    def describe(self):
        print(f"It is a circle with an area of {3,14 * self.radius * self.radius}cmˆ2")
        super().describe()

triangle = Triangle("red", True, 5, 6)
square = Square("green", False, 7)
circle = Circle("blue", False, 4)

triangle.describe()
print("-------------------------------")

square.describe()

print("-------------------------------")
circle.describe()

