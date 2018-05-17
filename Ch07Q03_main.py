from Ch07Q03_class import Account

def main():
    acc = Account(1122,20000,4.5)
    acc.withdraw(2500)
    acc.deposit(3000)
    print("ID:",acc.getId())
    print("Balance:",acc.getBalance())
    print("Monthly Interest Rate",acc.getMonthlyInterestRate())
    print("Monthly Interest",acc.getMonthlyInterest())
    
main()