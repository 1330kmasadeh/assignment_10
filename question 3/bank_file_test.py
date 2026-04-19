from bank_file import BankFile
from savingsaccount import SavingsAccount
from checkingaccount import CheckingAccount

bank = BankFile()

bank.add_account(SavingsAccount("Ali", "1111", 1000))
bank.add_account(CheckingAccount("Omar", "2222", 500))

bank.save()

print("Saved. Reloading...")

bank2 = BankFile()
bank2.display()
