class College:
    def __init__(self,ccode,cname):
        self.ccode=ccode
        self.cname=cname

    def set_ccode(self,ccode):
        self.ccode=ccode
    def get_ccode(self):
        return self.ccode
    def set_name(self,cname):
        self.cname=cname
    def __str__(self):
        return self.cname


    def display(self):
        return self.ccode,self.cname