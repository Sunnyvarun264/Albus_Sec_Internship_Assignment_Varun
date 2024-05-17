# Programmer Class

class Programmer:
    def __init__(self, name, age, company):
        self.name = name
        self.age = age
        self.company = company

    def __str__(self):
        return f"Programmer {self.name}, Age: {self.age}, Company: {self.company}"

# Example usage
programmer1 = Programmer("Alice", 30, "Microsoft")
programmer2 = Programmer("Bob", 25, "Microsoft")
print(programmer1)
print(programmer2)
