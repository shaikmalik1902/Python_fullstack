class Bank:
    def __init__(self):
        self.__balance = 5000 

    def show_balance(self):
        print("Balance:", self.__balance)


obj = Bank()

obj.show_balance()

print(obj.__balance)   