#print the number 1 to 5
for i in range(1,6):
    print(i)

#Sum of Even Numbers from 1 to n
n = 10
sum = 0
for i in range(1, n):
    if (i % 2 == 0):
        sum += i
print("Sum of even number: ", sum)

#multiplication table for n
n = 7
for i in range(1, 10):
    table = i * n
    print(f"{n}", " * "f"{i}", "=", table)

#Find Factorail of n
n = int(input("Enter a number: "))
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(factorial)

# check number is prime or not
n = int(input("Enter a number: "))
is_prim=True
if(n<=1):
    is_prime=False
else:
    for i in range(2, n + 1):
        if (n % i == 0):
            is_prime = False

if(is_prime):
    print(f"{n} is a prime number")
else:
    print(f"{n} is not a prime number")

#Fibanoic Series
print("---------Fibanoic Series----------")
a=0
b=1
n=10
for i in range(n):
    print(a,end=" ")
    a,b=b,a+b