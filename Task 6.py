class Bank:
    def __init__(self):
        self.__money = 1500

    def show_money(self):
        print("Money Available:", self.__money)


obj = Bank()
obj.show_money() 

class Bank:
    def __init__(self):
        self.__money = 1500

    def show_money(self):
        print("Money Available:", self.__money)

    def withdraw(self, amount):
        if amount > self.__money:
            print("Insufficient Balance")
        else:
            self.__money -= amount
            print("Money Available:", self.__money)


obj = Bank()

obj.show_money()
obj.withdraw(3000)