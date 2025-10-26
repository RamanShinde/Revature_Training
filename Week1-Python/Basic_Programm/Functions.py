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
    return "Hello to all!!"

print(greeting())

#Addition
def add(a,b):
    return a+b
print(add(3,4)) #Postional Argument

print(add(a=5,b=6)) # Keyword Argument


#Arbitary Argument:-
def addmultiple(*numbers):
    total=0
    for n in numbers:
        total+=n
    return total
print(addmultiple(1,2,3,4,5,6,7,8,9))
