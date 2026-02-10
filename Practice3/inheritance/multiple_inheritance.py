class Prey:

    def flee(self):
        print("This animal is fleeing")

class Predator:

    def hunt(self):
        print("This animal is hunting")

class Rabbit(Prey):
    pass

class Eagle(Predator):
    pass

class Fish(Prey, Predator):
    pass

rabbit = Rabbit()
eagle = Eagle()
fish = Fish()

rabbit.flee()
print("-------------------------------")

eagle.hunt()

print("-------------------------------")
fish.hunt()
fish.flee()