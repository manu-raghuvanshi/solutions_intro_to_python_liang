class Account:
    def __init__(self,id,balance,annualInterestRate):
        self.id=id
        self.balance=balance
        self.annualInterestRate=annualInterestRate
    
    def getId(self):
        return self.id
    
    def getBalance(self):
        return self.balance
      
    def getMonthlyInterestRate(self):
        return self.annualInterestRate/(12*100)
    
    def getMonthlyInterest(self):
        return  self.balance * self.getMonthlyInterestRate()
    
    def withdraw(self,sub):
        self.balance = self.balance - sub
        return self.balance
    
    def deposit(self,add):
        self.balance = self.balance + add
        return self.balance