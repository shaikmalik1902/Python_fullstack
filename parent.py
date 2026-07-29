class Father:
    def display(self):
        print("This is a parent class")


class Mother(Father):
    def show(self):
        print("This is a child class")


class Child(Mother):
    def show1(self):
        print("This is multiple inheritance")


obj = Child()

obj.display()
obj.show()
obj.show1()