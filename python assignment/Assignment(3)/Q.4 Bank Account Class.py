# Q.4 Create a Python class to represent a bank account with methods for deposit, withdrawal, and checking the balance.

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance is {self.balance}")
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}")
        else:
            print("Insufficient balance or invalid amount")

    def check_balance(self):
        return self.balance

# Example usage
account = BankAccount("Alice", 100)
account.deposit(50)
account.withdraw(30)
print("Balance:", account.check_balance())
