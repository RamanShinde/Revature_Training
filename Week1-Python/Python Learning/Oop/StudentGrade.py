
from Oop.StudDetails import StudentDetail
from Oop.studentextrcurr import StudExCur


ccode=int(input("Enter C-Code: "))
cname=input("Enter College Name: ")

rollno=int(input("Enter roll no: "))
name=input("Enter name: ")
m1=int(input("Enter m1: "))
m2=int(input("Enter m2: "))
m3=int(input("Enter m3: "))

exm1=int(input("Enter Exm1: "))
exm2=int(input("Enter Exm2: "))



#stud=StudentDetail(ccode,cname,rollno,name,m1,m2,m3 )
stud=StudExCur(ccode,cname,rollno,name,m1,m2,m3,exm1,exm2)
print("<--------------All Student Details-------------->")
print(f'college Code:-{stud.display()[0]}\n'
      f'College Name:-{stud.display()[1]}')
print(f'Roll No:{stud.get_rollno()}\n'
      f'Student Name:{stud.get_name()}\n'
      f'Studnet m1:{stud.get_m1()}\n'
      f'Studnet m2:{stud.get_m2()}\n'
      f'Studnet m3:{stud.get_m3()}\n'
      f'Total Makrs:{stud.calculate_total()}\n'
      f'Average Marks:{stud.calculate_avg()}'
      )
print(f'Extracurrecle Makrs{stud.calc_extort()}')
