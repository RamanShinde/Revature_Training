print("Hello World!!")
print("<----------------------Logic Operator--------------------->")
#logical operator
print(not 6)
print(not -6)
print(5>7 and 3<6)
print(6>3 and 4<3)
print(4>5 or 5>6)
print("<----------------------Bitwise Operator--------------------->")
# Bitwise Operator
print(5 & 7)
print(7 | 9)
print(7 ^ 9)
print("<----------------------Shift Operator--------------------->")
# shift operator
print(5<<3)
print(5<<4)
print(5>>2)
print("<----------------------Identity operator--------------------->")
# Identity operator
num1=10
print(type(num1))
print(num1 is int)
print(type(num1) is int)

#Concandation  <--in python can cancad the different type of datatype-->
#print("Raman"+10)
print("Raman: ",6)

print("<----------------------Casting--------------------->")
#Casting 
print("<----------------------Implocit Casting--------------------->")
#Implicit
print('implicit casting')
a=5
b=4.5
result=a+b
print(result)

print('Boolean to Integer')
print(True+10)
# Explicit
# a=input('Enter the number: ')
# t=float(a)
# print(t)

print("<----------------------String Operation--------------------->")
str1="hello there !"
print(str1[0])
print(str1[10])
print(str1[11])
print(str1[-1])
print(str1[-5])
print(str1[0:3])
print(str1[0:5:3])
print(str1[0::3])
print(str1[-3:-6])
print(str1[-6:-3])
print(str1[-10:-1:2])

print("<----------------------String Method--------------------->")
#It convert the first charcter as Captital
print(str1.capitalize())
#It convert the in String in whol upper case
print(str1.upper())
#It count the how many perticular charcter is present in String
print(str1.count('e'))
#Return the index of charcter if not then return the -1
print(str1.find('t'))
print(str1.find('s')) #op --> is -1
#Return the boolean value if string end with that charcter which want we check
print(str1.endswith('!'))
#Return the index of chartcer but if not find then it does not run the code shows err substirng not present
print(str1.index('t'))
#Convert String into List of name
print(str1.split())
#print(str1.split('a-z','A-Z'))
str2='12-12-2012'
print(str2.split('-')) # split with - remove these


a=5
b=6
if(a>b):
    print("a is greater than b")

else :
    print("b is greater then a")