'''
 --- Conditional Statement ---
 if
 if-else
 nested if,
 if else ladder
 Match case
'''
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
n=10
print(f"n is {n}")
if num1==num2:
    print("Both numbers are equal")
else:
    if num1 > num2:
        print(f"{num1}", "is greater than", f"{num2}")
    else:
        print(f"{num2}", "is greater than", f"{num1}")


# other way is write above program is use elif
print("---------Using Elif--------")
if num1==num2:
    print("Both numbers are equal")
elif num1 > num2:
        print(f"{num1}", "is greater than", f"{num2}")
else:
        print(f"{num2}", "is greater than", f"{num1}")
