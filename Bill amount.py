   
product = input("Enter product name: ")
quantity = int(input("Enter quantity: "))
price = float(input("Enter price per unit: "))

total = quantity * price
discount = total * 0.10 
final_amount = total - discount

print("\n BILL\n")
print(f"Product : {product}\n")
print(f"Quantity : {quantity}\n")
print(f"Price : {int(price) if price.is_integer() else price}\n")
print(f"Total : {int(total) if total.is_integer() else total}\n")
print(f"Discount : {int(discount) if discount.is_integer() else discount}\n")
print(f"Final Amount : {int(final_amount) if final_amount.is_integer() else final_amount}")