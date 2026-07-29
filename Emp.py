class Developer:
    def __init__(self, name, emp_id, language):
        self.name = name
        self.emp_id = emp_id
        self.language = language

    def display1(self):
        print(f"Name: {self.name}")
        print(f"Emp-id: {self.emp_id}")
        print(f"Programming language: {self.language}")


class Team(Developer):
    def __init__(self, name, emp_id, language, num):
        super().__init__(name, emp_id, language)
        self.num = num

    def display2(self):
        self.display1()
        print(f"Team no: {self.num}")


new = Team(101, "ravi", "python", 8)
new.display2() 