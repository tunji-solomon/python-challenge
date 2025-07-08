# ✅ Challenge: Simple Bank Account Class
# Write a class called BankAccount that does the following:

# 1️⃣ The class should have two attributes:

# account_holder (string) — the name of the account holder

# balance (float) — starting at 0 by default

# 2️⃣ The class should have three methods:

# deposit(amount) — adds the amount to the balance

# withdraw(amount) — subtracts the amount from the balance only if there are enough funds, otherwise print "Insufficient funds"

# display_balance() — prints the current balance in this format: "Current balance: $<balance>"

# 3️⃣ Do not use property decorators or fancy things — just simple __init__ and method logic.

class BankAccount:
    
    def __init__(self, account_holder : str):
        self.account_holder = account_holder
        self.balance : float = 0.0
        
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds")
            
    def display_balance(self):
        print(f"Current balance: ${self.balance}")
        
    

account = BankAccount("Alice")
account.deposit(100)
account.withdraw(30)
account.withdraw(100)  # Should print: Insufficient funds
account.display_balance()  # Should print: Current balance: $70.0


