class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, gpa):
        super().__init__(name)
        self.gpa = gpa

    def display(self):
        return f"Student: {self.name}, GPA: {self.gpa}"

P, G = input().split()
G = float(G)
student = Student(P, G)
print(student.display())