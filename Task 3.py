class Person:
    def __init__(self):
        self.name = "Naveen"
        self.age = 23


class Employee(Person):
    def __init__(self):
        super().__init__()
        self.salary = 50000

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Salary:", self.salary)


employee = Employee()
employee.display() 