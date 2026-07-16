#create account class with 2 attributes-balance& account no.
#create methods for debit,credit & printing the balance
class Account:
    def __init__(self,bal,acc):
        self.balance=bal
        self.account_no=acc

    def debit(self,amount):
        self.balance-=amount
        print("Rs.",amount,"was debited")
        print("total balance=",self.get_balance())

    def credit(self,amount):
        self.balance+=amount
        print("Rs.",amount,"was credited")
        print("total balance=",self.get_balance())

    def get_balance(self):
        return self.balance

acc1=Account(10000,22765)
acc1.debit(5000)
acc1.credit(6000)



