#The __init__() method is used to assign values to object properties,
# or to perform operations
# that are necessary when the object is being created.

#1

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Yerassyl", 18)

print(p1.name)
print(p1.age)

print("-------------------------------")

#2

class Info:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Info("Emil", 17)
p2 = Info("Lamar", 18)

print(p1.name, p1.age)
print(p2.name, p2.age)

print("-------------------------------")

#3

class Info1:
    def __init__(self, name, age, city, hobby):
        self.name = name
        self.age = age
        self.city = city
        self.hobby = hobby

p1 = Info1("Fred", 22, "Los Angeles", "american football")
p2 = Info1("Alex", 20, "Las Vegas", "casino")

print(p1.name,":", p1.hobby)
print(p2.name,":", p2.city)

print("-------------------------------")
#4

class Person1:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        return f"Here we go {self.name}!"

p1 = Person1("Yerassyl")
print(p1.greeting())