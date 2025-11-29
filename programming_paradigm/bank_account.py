class bankAccount:
    def __init__(self, initial_balance: float = 0.0):
        self._account_balance = float(initial_balance)


    def deposit(self, amount: float) -> None:
        if amount > 0:
            self._account_balance += amount
        else:
            raise ValueError("Deposit amount must be positive.")

    def withdraw(self, amount: float) -> bool:
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")

        if amount <= self._account_balance:
            self._account_balance -= amount
            return True
        else:
            return False
    def display_balance(self) -> None:
         
         print(f"Current Balance: ${self._account_balance:.2f}")
    