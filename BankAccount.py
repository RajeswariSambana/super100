class BankAccount:
    def __init__(self, account_holder, account_number, balance=None):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit of {amount} Rupees is successful. New balance: {self.balance}/-")
        else:
            print("Invalid deposit. Please deposit a positive amount.")
    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrawal of {amount} Rupees is successful.New balance: {self.balance}/-")
            else:
                print("Insufficient Money. Withdrawal unsuccessful.")
        else:
            print("Invalid, Please withdraw a positive amount.")
    def display_balance(self):
        print(f"Current balance for account {self.account_number}: {self.balance}/-")

account1 =BankAccount("Anu",987654321,1000)
account1.display_balance()
account1.deposit(500)
account1.withdraw(303)
account1.withdraw(2000)
account1.display_balance()

print("\n Another Account holder\n")
account2 =BankAccount("Vinay",123456789,500)
account2.deposit(250)
account2.withdraw(300)
account2.display_balance()
