a = [1,10,30,9,60,20,25]
b = list(filter(lambda x: x%2 !=0,a))
c = list(map(lambda x: x**2,a))
print(b)
print(c)