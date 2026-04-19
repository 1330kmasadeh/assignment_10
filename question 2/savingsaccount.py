from bankaccount import BankAccount

class SavingsAccount(BankAccount):
    def __init__(self, name, pin, balance=0, rate=0.02):
        super().__init__(name, pin, balance)
        self.rate = rate

    def compute_interest(self):
        self._balance += self._balance * self.rate

    def __str__(self):
        return f"Savings: {self._name}, Balance: {self._balance}"
