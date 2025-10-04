import sys
from bank_account import BankAccount


def main():
    account = BankAccount(100.0)
    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, balance")
        sys.exit(1)

    command, *params = sys.argv[1].split(":")
    amount = float(params[0]) if params else None
    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${amount}")
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount}")
        else:
            print("Insufficient funds")
    elif command == "balance":
        account.display_balance()
    else:
        print("Invalid command or missing amount")


if __name__ == "__main__":
    main()
