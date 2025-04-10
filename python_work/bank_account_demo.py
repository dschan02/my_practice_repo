#import bank_account.py file
from bank_account import BankAccount

account1 = BankAccount("1234", 1000)  #default balance is zero as defined in the __init__
print(account1)

BankAccount.deposit(account1, 100)
print(account1)

BankAccount.withdraw(account1, 300)
print(account1)

account2 = BankAccount("1111", 10)
BankAccount.deposit(account2, 9034)
print(f"account2 balance is ${BankAccount.get_balance(account2)}.")
