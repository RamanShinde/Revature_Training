num=str(input("Enter a number:"))
l=len(num)
n=int(num)
print(num)
rev=0
while(n > 0):
    rest=n%10
    rev=rev*10+rest
    n=n//10

print("Revsersed Number: ",rev)

sum=0
for i in range(1,8):
    sum+=i*i
print("Sum of each number with power:-",sum)

# Access
ls=[10,20,30,40,50]
for n in ls:
    print(n)

# Create new lst where square number stored
sqr=[]
for n in ls:
    sqr.append(n*n)
print(sqr)

# tuple operation
tu=(1,2,3,4,5)
print(tu)
tuls=[]
for n in tu:
    tuls.append(n)
print(tuls)
'''
To convert the tuple->List we can do by two way
1:-by append create new list and apppend
2:-By change the datatype li=list(tu)
'''
tulist=list(tu)
print(tulist)

#Set
