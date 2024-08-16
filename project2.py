class Account:
    def __init__(self,bal,acc):
        self.balance=bal
        self.account_no=acc
    #debit method
    def debit(self,ammount):
        self.balance-=ammount
        print('Rs.',ammount, 'was debited.')
        print('total bal is ',self.get_bal())
    # credit method
    def credit(self,ammount):
        self.balance+=ammount
        print('Rs.',ammount, 'was credited.')
        print('total bal is ',self.get_bal())
    #final bal
    def get_bal(self):
        return self.balance
acc1=Account(10000,12345)
acc1.debit(1000)
acc1.credit(500)
acc1.credit(150000)
