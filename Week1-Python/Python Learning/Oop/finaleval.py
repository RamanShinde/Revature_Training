from Oop.StudDetails import StudentDetail
from Oop.studentextrcurr import StudExCur
from Oop.teacherdetails import TeacherDetails


class FinalEval(StudExCur,TeacherDetails):
    def __init__(self,ccode,cname,rollno,sname,m1,m2,m3,exm1,exm2,empid,tname,dept,feedback):
        StudentDetail.__init__(self,ccode,cname,rollno,sname,m1,m2,m3)
        StudExCur.__init__(self,ccode,cname,rollno,sname,m1,m2,m3,exm1,exm2)
        TeacherDetails.__init__(self,ccode,cname,empid,tname,dept)
        self.__feedback=feedback
    @property
    def feedback(self):
        return self.__feedback
    @feedback.setter
    def feedback(self,feedback):
        self.__feedback=feedback

    # def display(self):
    #     return (f"{self.ccode},{self.cname},{self.empid},{self.tname}\n"
    #             f"")