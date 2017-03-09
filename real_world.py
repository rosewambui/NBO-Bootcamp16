"""the savings and current account inherites from bank account"""
class BankAccount(object):
        def deposit():
            pass

        def withdraw():
            pass


class SavingsAccount(BankAccount):
    def __init__(self):
        self.balance = 1000


    def deposit(self, amount):
        if (amount < 0):
            return "invalid deposit amount"
        else:
            self.balance +=amount
            return self.balance

    def withdraw(self, amount):
        if (self.balance - amount) < 1000:
            return "cannot withdrwal beyond the minimum account balance"
        elif amount > self.balance:
            return "cannot withdraw beyond the current account balance"
        elif amount < 0:
            return "invalid withdraw amount"
        else:
            self.balance -= amount
            return self.balance

class CurrentAccount(BankAccount):
    def __init__(self):
        self.balance=0

    def deposit(self, amount):
        if amount < 0:
            return "invalid deposit amount"
        else:
            self.balance =+ amount
            return self.balance
		    
    def withdraw(self,amount):
        if amount < 0:
            return "invalid withdraw amount"
        elif self.balance < amount:
            return "cannot withdraw beyond the current account balance"
        else:
            self.balance -= amount
            return self.balance
