from Oop.College import College


class TeacherDetails(College):
    def __init__(self,ccode,cname,empid,tname,dept):
        College.__init__(self,ccode,cname)
        self.__empid=empid
        self.__tname=tname
        self.__dept=dept


    @property
    def empid(self):
        return self.__empid
    @empid.setter
    def empid(self,empid):
        self.__empid=empid

    @property
    def tname(self):
        return self.__tname
    @tname.setter
    def tname(self,tname):
        self.__tname=tname

    @property
    def dept(self): #Getter
        return self.__dept
    @dept.setter
    def dept(self,dept): #Setter
        self.__dept=dept

    def display_tacher(self):
        '''Diply the Details of Tachner'''
        return(f'College Code:-{super().ccode}\n'
               f'College Name:-{super().cname}\n'
               f'Employee Id:-{self.empid}\n'
               f'Emplooyee Name:-{self.tname}\n'
               f'Department:-{self.dept}')
