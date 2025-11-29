
class BankAccount:
    def __init__(self, initial_balance=0):
        self._account_balance = float(initial_balance)

    def deposit(self, amount):
        amount = float(amount)
        if amount > 0:
            self._account_balance += amount
            print(f"Deposited: ${amount:g}")
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        amount = float(amount)
        if amount > 0:
            if amount <= self._account_balance:
                self._account_balance -= amount
                print(f"Withdrew: ${amount:g}")
                return True
            else:
                print("Insufficient funds.")
                return False
        else:
            print("Withdrawal amount must be positive")
            return False

    def display_balance(self):
        print(f"Current Balance: ${self._account_balance:g}")