class BankAcc:
    def __init__(self):
        self.acc_no=input()
        self.balance=float(input())
        self.date=input()
        self.customer_name=input("customer name:")
    def deposite(self):
        amount=float(input())
        self.balance+=self.amount
        print("balance is",self.balance)
    def withdraw(self,amount):
        amount2=float(input())
        if(balance<=amount2):
            self.balance-=self.amount2
            print("deposite",self.nbalance)
        else:
            print("insufficient amount")
    def check_amount(self):
        print(self.balance)
obj=BankAcc()
obj.deposite()
obj.withdraw()
obj.check_balance()