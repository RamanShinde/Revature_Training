'''
Lamda Function:-Is a small and anonymous function(function without name) is called lambada
It used when we want short function for short time period

Syntax:-
-->varible = lambda arguments:expression<--
'''

#Example 1
add=lambda a,b:a+b
sub=lambda a,b:a-b
mul=lambda a,b:a*b
div=lambda a,b:a/b
print(add(1,2))
print(sub(5,4))
print(mul(3,4))
print(div(6,4))

#Example 2
sqr=lambda x:x*x
print(f"Square is:{sqr(5)}")

#Example 3
res=lambda x,y:2*x+5*y+7
print(f"Res is:{res(3,2)}")