students = {
    "Ravi": 45,
    "Sita": 75,
    "Rahul": 35,
    "Anu": 60,
    "Kiran": 40
}

print("Students who scored below 50:")

for name, marks in students.items():
    if marks < 50:
        print(name, ":", marks)