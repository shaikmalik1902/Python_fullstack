class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display(self):
        print(f"Product: {self.name}")
        print(f"Price: {self.price}")


class Clothing(Product):
    def __init__(self, name, price, warranty):
        super().__init__(name, price)
        self.warranty = warranty

    def display1(self):
        self.display()
        print(f"Warranty: {self.warranty} years")


l = Clothing("shirt", 2000, 1)
l.display1()