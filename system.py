class bankaccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def get_balance(self):
        return self.balance

my_account = bankaccount('123456789', 'Ali Reza', 1000)
my_account.deposit(500) 
my_account.deposit(500)
print(f"new walet balance{my_account.account_holder}: {my_account.get_balance()}")
