class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        
    def display_balance(self):
        return f"Na účtě máte:{self.balance} Kč."
        
    def deposit(self, amount):
        self.balance += amount
        
account = BankAccount ("John Doe",1000)    
account.deposit (500)
print(account.balance)