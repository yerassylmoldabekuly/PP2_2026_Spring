#1
#A Class is like an object constructor, or a "blueprint" for creating objects.

class MyClass():
    x = 5
    y = 10
    z = 15

print("-------------------------------")

#2

p1 = MyClass() #Now we can use the class named MyClass to create objects:
p2 = MyClass()
print(p1.x)
print(p2.y)

print("-------------------------------")

#3

del p1

print("-------------------------------")

#4

p3 = MyClass()
p4 = MyClass()

print(p2.x)
print(p3.y)
print(p4.z)
