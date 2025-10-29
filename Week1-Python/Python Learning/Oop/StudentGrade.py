
# from Oop.StudDetails import StudentDetail
# from Oop.studentextrcurr import StudExCur
# from Oop.teacherdetails import TeacherDetails
from Oop.finaleval import FinalEval

ccode=int(input("Enter C-Code: "))
cname=input("Enter College Name: ")
#
rollno=int(input("Enter roll no: "))
sname=input("Enter name: ")
m1=int(input("Enter m1: "))
m2=int(input("Enter m2: "))
m3=int(input("Enter m3: "))

exm1=int(input("Enter Exm1: "))
exm2=int(input("Enter Exm2: "))
#
#
#
# #stud=StudentDetail(ccode,cname,rollno,name,m1,m2,m3 )
# stud=StudExCur(ccode,cname,rollno,name,m1,m2,m3,exm1,exm2)
# print("<--------------All Student Details-------------->")
# print(f'college Code:-{stud.display()[0]}\n'
#       f'College Name:-{stud.display()[1]}')
# print(f'Roll No:{stud.get_rollno()}\n'
#       f'Student Name:{stud.get_name()}\n'
#       f'Studnet m1:{stud.get_m1()}\n'
#       f'Studnet m2:{stud.get_m2()}\n'
#       f'Studnet m3:{stud.get_m3()}\n'
#       f'Total Makrs:{stud.calculate_total()}\n'
#       f'Average Marks:{stud.calculate_avg()}'
#       )
# print(f'Extracurrecle Makrs{stud.calc_extort()}')

empid=int(input("Enter Employee ID: "))
tname=input("Enter Teacher Name: ")
dept=input("Enter Department Name: ")


# teacher=TeacherDetails(ccode,cname,empid,tname,dept)
# print("------>Details of Teacher<------")
# print(teacher.display())

feedback=input("Enter feedback: ")
finaleval=FinalEval(ccode,cname,rollno,sname,m1,m2,m3,exm1,exm2,empid,tname,dept,feedback)

print(f'Collge details:-{finaleval.display()}')
print(f'Teacher Details:-{finaleval.display_tacher()}')
print(f'Student Rollno:{finaleval.rollno}')
print(f'Student Sname:{finaleval.sname}')
print(f'Student M1:{finaleval.m1}')
print(f'Student M2:{finaleval.m2}')
print(f'Student M3:{finaleval.m3}')
print(f'Student Exm1:{finaleval.exm1}')
print(f'Student Exm2:{finaleval.exm2}')
print(f'Student Total Marks:-{finaleval.calculate_total()}')
print(f'Student Average Marks:-{finaleval.calculate_avg()}')
print(f'Student etra culleculare:-{finaleval.calc_extort()}')

