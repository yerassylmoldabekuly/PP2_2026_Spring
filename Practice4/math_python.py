#1
import math

degree = int(input())
pie = math.pi
to_radian = degree * pie/180

print("Output radian:", to_radian)

print("\n")
print("--------------------------")

#2

height = 5
base1 = 5
base2 = 6

area_of_trapezoid = (base1 + base2)/2 * height
print("Area of a trapezoid:", area_of_trapezoid)

print("\n")
print("--------------------------")

#3

n = 4
s = 25

area = (n * s**2)/4 * math.tan(math.pi/n)

print("The area of the polygon is:", math.ceil(area))

print("\n")
print("--------------------------")

#4

base = 5
height = 6
area = base * height

print(f"Area of a parallelogram: {area}")



