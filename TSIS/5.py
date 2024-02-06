class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposit of ${} accepted. Current balance: ${}".format(amount, self.balance))
        else:
            print("Deposit amount must be greater than 0.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print("Withdrawal of ${} accepted. Current balance: ${}".format(amount, self.balance))
            else:
                print("Insufficient funds. Withdrawal amount exceeds available balance.")
        else:
            print("Withdrawal amount must be greater than 0.")

account = BankAccount("John Doe", 1000)
account.deposit(500)
account.withdraw(200)
account.deposit(1000)
account.withdraw(1500)
account.withdraw(300)
account.withdraw(2000)