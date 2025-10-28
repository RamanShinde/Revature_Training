
from Oop.College import College

class StudentDetail(College):
    def __init__(self,ccode,cname,rollno,sname,m1,m2,m3):
        super().__init__(ccode,cname)
        super().display()
        self.rollno=rollno
        self.sname=sname
        self.m1=m1
        self.m2=m2
        self.m3=m3

    def calculate_total(self):
        total=self.m1+self.m2+self.m3
        return total

    def calculate_avg(self):
        return self.calculate_total()/3

    def get_rollno(self):
        return self.rollno
    def set_rollno(self,rollno):
        self.rollno=rollno

    def get_name(self):
        return self.sname
    def set_name(self,sname):
        self.sname=sname

    def get_m1(self):
        return self.m1
    def set_m1(self,m1):
        self.m1=m1

    def get_m2(self):
        return self.m2
    def set_m2(self,m2):
        self.m2=m2

    def get_m3(self):
        return self.m3
    def set_m3(self,m3):
        self.m3=m3


'''
Access modifier
public:-Any one can acces from any package {self.name}
private:-Only within the same class not even from same package {self.__name} denote by DoubleUnderScore(__)
Protected:-Within same package and the class which is child {Self._name} denote by UnderScore

Inheritance:-
In Python there is no extend like extend like in java so just do
    classname(parentClassname):->this is inheritance is called 
    super().__init__(ccode,cname)=>which is used to access the parent class field and methods
    super().display()
'''

