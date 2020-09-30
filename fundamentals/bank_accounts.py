class BankAccount:
    def __init__(self, int_rate=0.01, balance=0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        if self.balance < 0:
            print(f"Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self

    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.int_rate * self.balance)
        return self


acct_1 = BankAccount()
acct_2 = BankAccount()

acct_1.deposit(100).deposit(100).deposit(100).withdraw(
    200).yield_interest().display_account_info()

acct_2.deposit(500).deposit(500).withdraw(100).withdraw(100).withdraw(
    100).withdraw(100).yield_interest().display_account_info()
