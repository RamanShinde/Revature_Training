from Exception_Handling.agenoterror import AgeNotEnoughError
from Exception_Handling.arithcalculation import ArithCalculation
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
age=int(input("Enter age: "))

cal=ArithCalculation(num1,num2)

print(f"Addition is:-{cal.add()}")
print(f"Subtraction is:-{cal.sub()}")
print(f"Multiplication is:-{cal.multiply()}")

try:
    if num2==0:
         raise ZeroDivisionError
    if(age<18):
        raise AgeNotEnoughError("Age should be more than 18")
except ZeroDivisionError as zde:
    print(f"{zde}:-0 is in denominator")
except AgeNotEnoughError as agne:
    print(f"{agne}")
else:
    try:
        print(f"Division in Float:-{cal.divide()}")
        print(f"Division in Integer:-{cal.idivide()}")
        l1 = [1, 5, 7, 3]
        val = l1[10]
    except IndexError as ie:
        print(f"{ie}:-Index is out of range")
    else:
        print(val)
    finally:
        print("Code Run EveryTime!!")
