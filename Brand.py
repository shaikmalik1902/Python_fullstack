class Call:
    def calling(self):
        print("calling....")


class Capture:
    def capturing(self):
        print("capturing image...")


class Brand(Call, Capture):
    def __init__(self, smartphone):
        self.smartphone = smartphone

    def display(self):
        print(f"Brand: {self.smartphone}")
        self.calling()
        self.capturing()


b = Brand("iphone")
b.display()