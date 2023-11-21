from bank_account import BankAccount

account = BankAccount("019789", 1000)
print(account)

account.deposit(100)
print(account)

account.withdraw(50)
print(account)

print("The account's balance is", account.get_balance())

account2 = BankAccount("024338", 4400)
print(account,", and",account2)