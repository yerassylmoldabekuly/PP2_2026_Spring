#1

class Animal:

    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is asleep")

#2

class Dog(Animal):

    def speak(self):
         return "WOOF"


#3

class Cat(Animal):

    def speak(self):
        return "MEOW"

#4

class Mouse(Animal):

    def speak(self):
        return "SQUEEK"


dog = Dog("Scooby")
cat = Cat("Tommy")
mouse = Mouse("Micky")

print(dog.speak())
print(cat.speak())
print(mouse.speak())
print("-------------------------------")

dog.eat()
dog.sleep()

print("-------------------------------")

cat.eat()
cat.sleep()

