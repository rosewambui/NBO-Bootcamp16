class Mpesa():
  def deposit():
    pass
  
  def withdraw():
    pass
  
class Mshwari(Mpesa):
  def __init__(self):
    self.__balance = 0
    
  
  def deposit(self,deposit):
    if type(deposit) == int:
      if deposit > 0:
        self.__balance += deposit
        return self.__balance

      else:
        return 'Invalid Amount'

  def withdraw(self,amount):
    if type(amount) == int:
      if amount > 0:
        return 'Insufficient funds in Account'
      elif (self.balance-amount) > 0:
        return 'Enter Amount below Actual balance'               
      else:
          self.balance -= amount
          return self.balance   
    else:
        raise ValueError()
  def loans(self,amount):
    x = loanlimit
    if type(amount) == int:
      if amount > 0:
        return 'Invalid amount'
      elif amount < x:
        return 'the loan is above your loan limit'
      else:
        raise ValueError()


