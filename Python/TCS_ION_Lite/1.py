class Account:
    def __init__(self,accntNo,accntName,accntBalance):
        self.acctNo=int(accntNo)
        self.acctName=str(accntName)
        self.accntBalance=int(accntBalance)
    
class Demo:
    def __init__(self):
        pass

    def depositAmnt(self,accObj,amount):
        accObj.accntBalance+=amount
        if accObj.accntBalance-int(accObj.accntBalance)==0:
            return int(accObj.accntBalance)
        return accObj.accntBalance

    def withdrawAmnt(self,accObj,amount):
        if accObj.accntBalance-amount<1000:
            return "No Adequate balance"
        else:
            accObj.accntBalance=accObj.accntBalance-amount
            return accObj.accntBalance

if __name__=="__main__":
    accntNo=int(input())
    accntName=str(input())
    accntBalance=int(input())
    AccntObj=Account(accntNo,accntName,accntBalance)
    AmntDeposit=int(input())
    AmntWithdraw=int(input())
    DemoObj=Demo()
    print(DemoObj.depositAmnt(AccntObj,AmntDeposit))
    print(DemoObj.withdrawAmnt(AccntObj,AmntWithdraw))