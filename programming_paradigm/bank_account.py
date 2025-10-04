class BankAccount:
    def __init__(self, initial_balance: float = 0.0):
        self.account_balance = initial_balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.account_balance += amount

    def withdraw(self, amount: float) -> bool:
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.account_balance:
            return False
        self.account_balance -= amount
        return True

    def display_balance(self) -> float:
        print(f"Current Balance: ${self.account_balance}")
        return self.account_balance

    def __str__(self) -> str:
        return f"Account balance : ${self.account_balance:.2f}"
