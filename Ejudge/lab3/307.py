import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        return f"({self.x}, {self.y})"

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

        return f"({self.x}, {self.y})"

    def dist(self, other_point):
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

point = Point(x1, y1)
print(point.show())
print(point.move(x2, y2))

other = Point(x3, y3)
result = point.dist(other)
print(f"{result:.2f}")

