class BankAccount:
    def __init__(self, name, pin, balance=0):
        self._name = name
        self._pin = pin
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount > self._balance:
            return "Insufficient funds"
        self._balance -= amount
