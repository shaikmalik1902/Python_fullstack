file = open('notes.txt','w') 
file.write("hello \n")
file.write("world")
file.close()

file = open('notes.txt','r')
content = file.read()
print(content)
file.close()

with open('notes.txt','a')  as f:
    f.written