'''
Syntax:-
def function_Name(x):   #x=> is argument
     print(What we want to print)


Arguments types
Positional Arguments:-Must be passed in the correct order
Keyword Arguments:-Passed using parameter names
Default Arguments:-Have a default value if not provided
Arbitary arguments:-Used when you don’t know how many arguments will be passed. (*x)

'''
#Greating
def greeting():
    ''' Return the greeting the message '''
    return "Hello to all!!"

print(greeting())

#Addition
def add(a,b):
    """ Return the sum of two numbers """
    return a+b
print(add(3,4)) #Postional Argument

print(add(a=5,b=6)) # Keyword Argument


#Arbitary Argument:- It stored the value in the list
def addmultiple(*numbers):
    """Find the sum of multiple numbers"""
    total=0
    for n in numbers:
        total+=n
    return total
print(addmultiple(1,2,3,4,5,6,7,8,9))

x="Raman",1,3.55
y=tuple(x)
print(y)
print(20/10)

#Arbitary Keyword arguments:-It stores the number in Dictonary
def keyword(** numbers):
    """Print the value of Keyword arguments"""
    for key,value in numbers.items():
        print(key,":",value)

print(keyword(name="Raman",age=24,job="Data Engineer"))

# Calaculate Function
def calculate(m1,m2,m3):
    """Calculates total and average of 3 marks."""
    total_Marks=m1+m2+m3
    avg_Marks=total_Marks/3
    return avg_Marks,total_Marks

m1=int(input("Enter first number: "))
m2=int(input("Enter second number: "))
m3=int(input("Enter third number: "))

total,avg=calculate(m1,m2,m3)
print(f'total:{total} Avg:{avg}')

