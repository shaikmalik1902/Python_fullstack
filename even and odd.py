
num_str = input("Input\n\n")

total_digits = len(num_str)

even_count = 0
odd_count = 0

for char in num_str:
    if char.isdigit():
        digit = int(char)
        if digit % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

print("\nOutput\n")
print(f"Digits = {total_digits}\n")
print(f"Even Digits = {even_count}\n")
print(f"Odd Digits = {odd_count}")