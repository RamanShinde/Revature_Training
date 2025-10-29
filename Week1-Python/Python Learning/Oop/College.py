
from unittest.mock import PropertyMock


class College:
    def __init__(self,ccode,cname):
        self.__ccode=ccode
        self.__cname=cname

    # def set_ccode(self,ccode):
    #     self.__ccode=ccode
    # def get_ccode(self):
    #     return self.ccode
    # def set_name(self,cname):
    #     self.__cname=cname
    # def get_Cname(self):
    #     return self.cname

    @property
    def ccode(self):
        return self.__ccode
    @ccode.setter
    def ccode(self,ccode):
        self.__ccode=ccode

    @property
    def cname(self):
        return self.__cname
    @cname.setter
    def cname(self,cname):
        self.cname=cname



    def display(self):
        return self.ccode,self.cname
