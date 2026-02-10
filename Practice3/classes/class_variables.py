#1

class Student:
    school = "KBTU" # class variable

p1 = Student()
p2 = Student()

print(p1.school)
print(p2.school)

print("----------------------------------------------")

#2

class Car:
    model = "Tesla" # class variable

c1 = Car()
c2 = Car()

Car.model = "Mercedes"

print(c1.model)
print(c2.model)

print("----------------------------------------------")

#3

class User:

    role = "User" # class variable

    def __init__(self, name):
            self.name = name

p1 = User("Zhan")
p2 = User("Aman")

print(p1.name, p1.role)
print(p2.name, p2.role)

print("----------------------------------------------")

#4

class Player:
    level = 1 # class variable

p1 = Player()
p2 = Player()

p1.level = 5

print(p1.level)
print(p2.level)

print("----------------------------------------------")

#5

class Account:
    total_accounts = 0

    def __init__(self):
        Account.total_accounts += 1

p1 = Account()
p2 = Account()
p3 = Account()

print(Account.total_accounts)



