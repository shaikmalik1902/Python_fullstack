class Triangle:
    def __init__(self, b, h):
        self.b = b
        self.h = h

    def area(self):
        return 0.5 * self.b * self.h


c = Triangle(10, 20)
print(c.area())