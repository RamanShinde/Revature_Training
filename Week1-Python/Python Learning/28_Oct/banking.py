'''Banking Interest Calculations'''

from interrest_calculation  import simple_interest,compound_interest
#from class-Name import method name/* means all method in all

prin=float(input("enter the principle value:-"))
ny=float(input("enter the number of years:-"))
roi=float(input("enter the roi:-"))
n=float(input("enter the number times compounded per years:-"))

si,amount=simple_interest(prin=prin,ny=ny,roi=roi)
print(f'Simple Interest:{si} :: Amount:{amount}')

compound_amt=compound_interest(prin=prin,ny=ny,roi=roi,n=n)
print(f'Compound_Interest:{compound_amt}')
