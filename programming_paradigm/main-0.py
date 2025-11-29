import sys
from bank_account import BankAccount


def main():
    account = BankAccount(100.0)

    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands:")
        print("  deposit:<amount>    - Deposit money")
        print("  withdraw:<amount>   - Withdraw money")
        print("  display             - Show current balance")
        sys.exit(1)

    arg = sys.argv[1]
    
    if ':' in arg:
        command, amount_str = arg.split(':', 1)
        try:
            amount = float(amount_str)
        except ValueError:
            print("Error: Amount must be a valid number.")
            sys.exit(1)
    else:
        command = arg
        amount = None

    if command == "deposit" and amount is not None:
        try:
            account.deposit(amount)
            print(f"Deposited: ${amount:.2f}")
        except ValueError as e:
            print(f"Error: {e}")

    elif command == "withdraw" and amount is not None:
        try:
            success = account.withdraw(amount)
            if success:
                print(f"Withdrew: ${amount:.2f}")
            else:
                print("Insufficient funds.")
        except ValueError as e:
            print(f"Error: {e}")

    elif command == "display":
        account.display_balance()

    else:
        print("Invalid command.")
        print("Valid commands: deposit:<amount>, withdraw:<amount>, display")


if __name__ == "__main__":
    main()