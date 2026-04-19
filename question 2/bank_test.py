from bank import Bank
from savingsaccount import SavingsAccount
from checkingaccount import CheckingAccount

bank = Bank()

s = SavingsAccount("Ali", "1111", 1000)
c = CheckingAccount("Omar", "2222", 500)

bank.add_account(s)
bank.add_account(c)

bank.display()
bank.computeInterest()
print("\nAfter Interest:")
bank.display()
