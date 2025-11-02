
import numpy as np
angles=np.array([0,np.pi/2,np.pi])
print(angles)

values=np.array([1,2,3])
print(f"Exponetial function of values, {np.exp(values)}")
print(f"Natural log of values, {np.log(values)}")
print(f"Base-10 log of values, {np.log10(values)}")

print("Modulus of 5 and 2 ",np.mod(5,2))
print("Remainder of 5 and 3 ",np.remainder(5,3))
print(5%2)


'''
Linear Algebra Functions
Dot Product and Matrix Multiplication
Determinants and Inverses
Eigenvalues and Eigenvectors
'''

a=np.array([[1,2],[3,4]])
b=np.array([[5,6],[7,8]])
print("Dot product of A and B:", np.dot(a, b))
print("Matrix multiplication of A and B:", np.matmul(a, b))

print("Determinant of A:", np.linalg.det(a))
print("Inverse of A:\n", np.linalg.inv(a))

eigenvalues, eigenvectors = np.linalg.eig(a)
print("Eigenvalues of A:", eigenvalues)
print("Eigenvectors of A:\n", eigenvectors)

from scipy import stats
data=np.array([1,2,3])
