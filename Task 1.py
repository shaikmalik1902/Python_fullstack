
class Animal:
    def eat(self):
        print("Animal eats food")

class Bird(Animal):
    def fly(self):
        print("Bird can fly")

class Parrot(Bird):
    def speak(self):
        print("Parrot can speak")

p = Parrot()

p.eat()
p.fly()
p.speak()