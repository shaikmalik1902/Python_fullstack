class Person:
    def display_name(self):
        print("Name: Rahul")


class Student(Person):
    def display_roll_no(self):
        print("Roll No: 101")

s = Student()
 
s.display_name()
s.display_roll_no()