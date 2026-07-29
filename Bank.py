balance = 5000

while True:
    print("\n1. Check Balance\n2. Deposit\n3. Withdraw\n4. Exit")
    choice = input("\nChoose an option: ")

    if choice == '1':
        print(f"Balance: ₹{balance}")
    elif choice == '2':
        balance += float(input("Enter deposit amount: ₹"))
        print(f"Updated Balance: ₹{balance}")
    elif choice == '3':
        amount = float(input("Enter withdrawal amount: ₹"))
        if amount <= balance:
            balance -= amount
            print(f"Updated Balance: ₹{balance}")
        else:
            print("Insufficient Balance!")
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid Choice!")