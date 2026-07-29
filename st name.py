class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Course: {self.course}")


s = Student('name', 22, "pfsd")
s.display()