n1,n2,n3 = map(int, input("Enter the marks for three subjects: ").split())

total = n1 + n2 + n3
average = total / 3

print("Total marks:", total)
print("Average marks:", average)

if n1 >= 35 and n2 >= 35 and n3 >= 35:
    print("Pass")
else:
    print("Fail")