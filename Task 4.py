class Student:
    def __init__(self):
        self.name = "Malik"    
        self.marks = 92       

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)

obj = Student()
obj.display()