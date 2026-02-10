#1

class Animal:
    def speak(self):
        print("The animal makes a sound")

class Dog(Animal):
    def speak(self):
        print("WOOOW")


a = Animal()
d = Dog()

a.speak()
d.speak()

print("-------------------------------")

#2

class Vehicle:

    def move(self):
        print("The vehicle moves")

class Car(Vehicle):

    def move(self):
        super().move() #super() lets you extend, not replace
        print("The car drives on roads")

c = Car()
c.move()

print("-------------------------------")

#3

class Person:

    def __init__(self, name):
        self.name = name

class Student(Person):

    def __init__(self, name, university):
        super().__init__(name)
        self.university = university

student = Student("Yerassyl", "KBTU")

print(student.name, student.university)

print("-------------------------------")

#4

class Shape:
    def area(self):
        return 0

class Triangle(Shape):
    def area(self):
        return 5 * 10

triangle = Triangle()

print(triangle.area())

