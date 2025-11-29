# bank_account.py

class BankAccount:
    """
    A simple BankAccount class with deposit, withdraw and display_balance methods.
    """

    def __init__(self, initial_balance=0):
        self._balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited ${amount:.2f}")
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        if amount > 0:
            if self._balance >= amount:
                self._balance -= amount
                print(f"Withdrew ${amount:.2f}")
                return True
            else:
                print("Insufficient funds")
                return False
        else:
            print("Withdrawal amount must be positive")
            return False

    def display_balance(self):
        print(f"Current Balance: ${self._balance:.2f}")