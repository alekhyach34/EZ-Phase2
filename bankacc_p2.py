class BankAcc:
    def __init__(self):
        self.acc_no=input()
        self.balance=float(input())
        self.date=input()
        self.customer_name=input("customer name:")
    def deposite(self):
        amount=float(input())
        self.balance+=amount
        print("balance after deposition",self.balance)
    def withdraw(self):
        amount=float(input())
        if(self.balance>amount):
            self.balance-=amount
            print("withdrawed amount",self.balance)
        else:
            print("insufficient amount")
    def check_balance(self):
        print("available balance",self.balance)
obj=BankAcc()
obj.deposite()
obj.withdraw()
obj.check_balance()