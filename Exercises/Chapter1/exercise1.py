# Construct a class hierarchy for people on a college campus. Include faculty, staff, and students.
# What do they have in common? What distinguishes them from one another?

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, major, year):
        super().__init__(name, age)
        self.major = major
        self.year = year

class Undergraduate(Student):
    def __init__(self, name, age, major, year, gpa):
        super().__init__(name, age, major, year)
        self.gpa = gpa

class Graduate(Student):
    def __init__(self, name, age, major, year, gpa, thesis):
        super().__init__(name, age, major, year, gpa)
        self.thesis = thesis

class Employee(Person):
    def __init__(self, name, age, department, salary):
        super().__init__(name, age)
        self.department = department
        self.salary = salary
    
class Faculty(Employee):
    def __init__(self, name, age, department, salary, rank):
        super().__init__(name, age, department, salary)
        self.rank = rank

class Staff(Employee):
    def __init__(self, name, age, department, salary, title):
        super().__init__(name, age, department, salary)
        self.title = title