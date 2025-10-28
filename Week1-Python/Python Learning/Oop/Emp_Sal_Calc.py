
from Oop.Employee import Employee
employee=Employee(101,"Ashish",41000.00)
print(f'Employee Id:-{employee.empid}\n'
      f'Employee Name:-{employee.ename}\n'
      f'Employee Balance:-{employee.bp}\n')


empid=int(input('Enter the employee Id:-'))
ename=input('Enter the employee Name:-')
bp=float(input('Enter the Employee Balance:-'))

print(f'Employee Id:-{empid}\n Name:{ename}\n Balance:{bp}\n'
      f'Gross pay:{employee.calc_grosspay(bp)}\n'
      f'Net Pay:{employee.calc_netpay(bp)}')

emp2=Employee(102,"Raaj",40000.00)
print(emp2)