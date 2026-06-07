class BankAccount:
    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount

    def get_balance(self):
        print(f"{self.name} (Account: {self.account_number}) — Balance: Rs. {self.balance}")


# --- Setup ---
accounts = [
    ("Ramesh Thapa", "A001", 5000),
    ("Sunita Karki", "A002", 0),
    ("Bikash Rai",   "A003", 12000),
]

a001, a002, a003 = [BankAccount(name, acc, bal) for name, acc, bal in accounts]

# --- Transactions ---
a002.deposit(3000)           
a003.withdraw(15000)         
a001.withdraw(2000)          
# --- Final Balances ---
print("\n--- Final Balances ---")
a001.get_balance()
a002.get_balance()
a003.get_balance()