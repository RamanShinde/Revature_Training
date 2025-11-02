
import numpy as np

array1=np.array([1,2,3])
array2=np.array([4,5,6])

#Element wise addition
print("Element wise addition",array1+array2)
#Element wise substraction
print("Element wise substraction",array1-array2)
#Element wise multipliction
print("Element wise multiplication",array1*array2)
#Element wise divide
print("Element wise division",array1/array2)

#Multipy by n number:
print("Multiply by 10 ",array1*10)
print("Multiply by 10 ",array1*10)

#Sum of all element
print("Divide by 10 ",np.sum(array1))
#mean of all element
print("Mean of array",np.mean(array1))


'''
Broadcasting:-
Broadcasting is the concept in numpy where we can do operation on different size of array
Input:-
a1=np.array([1,2,3])
a2=np.array([[4],[5],[6]])
Op:-
[[5 6 7][6 7 8][7 8 9]]

[4]+[1,2,3,]=>[5 6 7] like other
'''

a1=np.array([1,2,3])
a2=np.array([[4],[5],[6]])

print(f"Bordcatsting sum:{a1+a2}")

'''
Vectoriztion:-
Vectoriztion allows us to perfrom operation on array without expliciting loop

'''
va=np.arange(1,6)
print(va)

vb=va+10
print("After Applying vectorization ",vb)

'''
np.where:it used to search any number from array
np.any: it check that the condition is satisfied or not if then return true not false
ex:-
np.any(array>5)
if above condition satisdfied then it will return the true
'''
index_of_one = np.where(va == 1)
print("Indices where element is 1:", index_of_one)

# Checking if any element is greater than 5
any_greater_than_five = np.any(va > 5)
print("Any element greater than 5:", any_greater_than_five)

# Checking if all elements are positive
all_positive = np.all(va > 0)
print("All elements are positive:", all_positive)


