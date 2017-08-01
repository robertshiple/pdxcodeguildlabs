# ATM class containing two attributes: a balance and an interest rate

# a newly created account will have a balance of 0 and Interest rate of 0.1%

# check_balance() returns the account balance

# deposit(amount) deposits the given amount in the account

#check_withdrawal(amount) returns true if the withdrawn amount won't put the account in the negative

#withdraw(amount) withdraws the amount from the account and returns it

#calc_interest() returns the amount of interest calculated on the account

import math

class Atm:

    def __init__(self):
        self.balance = 100
        self.interest = 0.1

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount

    def check_withdrawal(self, amount):
        if amount > self.balance:
            return False
        else:
            return True  

    def withdraw(self, amount):
        self.balance -= amount

    def calc_interest(self):
        return self.interest * self.balance

atm = Atm()
atm.check_balance()
atm.withdraw(10)
atm.deposit(10)
atm.calc_interest

check_money = input("welcome to bank. what do u want? ")
balance = atm.check_balance()
interest = atm.calc_interest()


if check_money == 'balance':
     print(balance)
elif check_money == 'deposit':
    amount = int(input("how much money do you want to add?: "))
    atm.deposit(amount)
    print('your new balance is ' + str(balance + amount))
elif check_money == 'withdraw':
    amount = int(input('how much would you like to withdraw? '))
    if atm.check_withdrawal(amount):
        atm.withdraw(amount)
        print('your new balance is ' + str(balance - amount))
    else:
        print('you don\'t have that much money')
elif check_money == 'interest':
    print(interest)
