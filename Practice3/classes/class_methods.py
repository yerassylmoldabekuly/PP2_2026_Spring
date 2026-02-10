#1

class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, {self.name}, Good luck!")

p1 = Person("Yerassyl")
p1.greet()

print("----------------------------------------------")

#2

class Calculator:

    def add(self, a, b):
        return a + b

    def substr(self, a, b):
        return a - b

    def mult(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b

calc = Calculator()

print(calc.add(5, 3))
print(calc.substr(5, 3))
print(calc.mult(5, 3))
print(calc.div(15, 3))

print("----------------------------------------------")

#3

class Person1:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        return f"{self.name} is {self.age} years old."

p1 = Person1("Darwin", 15)
print(p1.get_info())

print("----------------------------------------------")

#4

class Person2:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def celebrate_birth(self):
        self.age += 1
        return f"{self.name} just turned {self.age} :)"

p2 = Person2("Tomas", 16)
print(p2.celebrate_birth())
print(p2.celebrate_birth())
print(p2.celebrate_birth())

print("----------------------------------------------")

#5

class Playlist:

    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)
        print(f"Added: {song}")

    def del_song(self, song):
        self.songs.remove(song)
        print(f"The {song} was removed.")

    def show_songs(self):
        print(f"Playlist: {self.name}")
        for song in self.songs:
            print(f" - {song}")


my_playlist = Playlist(1)
my_playlist.add_song("I ain't worried")
my_playlist.add_song("Hate it Or love it")
my_playlist.add_song("sdp interlude")
my_playlist.del_song("I ain't worried")
print("----------------------------------------------")
my_playlist.show_songs()


