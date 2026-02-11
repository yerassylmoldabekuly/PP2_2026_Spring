class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    def total_salary(self):
        return self.base_salary

class Manager(Employee):

    def __init__(self, name, base_salary):
        super().__init__(name, base_salary)

    def total_salary(self, bonus_percent):
        return self.base_salary * (1 + bonus_percent/100)

class Developer(Employee):

    def __init__(self, name, base_salary):
        super().__init__(name, base_salary)

    def total_salary(self, completed_projects):
        return self.base_salary + completed_projects * 500


class Intern(Employee):

    def __init__(self, name, base_salary):
        super().__init__(name, base_salary)


    def total_salary(self):
        return self.base_salary

data = input().split()
employee = data[0]
name = data[1]
a = int(data[2])

if employee == "Intern":
    intern = Intern(name, a)
    print(f"Name: {intern.name}, Total: {intern.total_salary():.2f}")

else:
    b = int(data[3])

    if employee == "Manager":
        manager = Manager(name, a)
        print(f"Name: {manager.name}, Total: {manager.total_salary(b):.2f}")

    elif employee == "Developer":
        developer = Developer(name, a)
        print(f"Name: {developer.name}, Total: {developer.total_salary(b):.2f}")