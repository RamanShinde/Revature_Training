'''Create a employee class'''
class Employee:
    def __init__(self,empid,ename,bp):
        self.empid=empid
        self.ename=ename
        self.bp=bp
    def calc_allowance(self,bp):
        return (self.bp*0.1)+(self.bp*0.05)

    def calc_ded(self,bp):
        return self.bp*0.03
    def calc_grosspay(self,bp): #self is equal to the this keyword in java
        return  self.bp+self.calc_allowance(bp)
    def calc_netpay(self,bp):
        return self.calc_grosspay(bp)-self.calc_ded(bp)

