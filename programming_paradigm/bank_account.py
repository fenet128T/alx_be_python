class BankAccount:
    def __init__(self, initial_balance=0):
        self._account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self._account_balance += amount
            # Force clean output: no .0 when whole number
            if amount == int(amount):
                print(f"Deposited: ${int(amount)}")
            else:
                print(f"Deposited: ${amount}")
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive")
            return False
        if amount > self._account_balance:
            print("Insufficient funds.")
            return False
        
        self._account_balance -= amount
        if amount == int(amount):
            print(f"Withdrew: ${int(amount)}")
        else:
            print(f"Withdrew: ${amount}")
        return True

    def display_balance(self):
        balance = self._account_balance
        if balance == int(balance):
            print(f"Current Balance: ${int(balance)}")
        else:
            print(f"Current Balance: ${balance}")