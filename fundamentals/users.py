class User:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def make_deposit(self, amount):
        self.balance += amount
        return self

    def make_withdrawal(self, amount):
        self.balance -= amount
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.balance}\n")
        return self


user_1 = User("James", 1000)
user_2 = User("Rachel", 100)
user_3 = User("Harry", 0)

user_1.make_deposit(100).make_deposit(
    100).make_deposit(100).make_withdrawal(100).display_user_balance()

user_2.make_deposit(400).make_deposit(
    500).make_withdrawal(250).make_withdrawal(250).display_user_balance()

user_3.make_deposit(750).make_withdrawal(
    250).make_withdrawal(250).make_withdrawal(350).display_user_balance()
