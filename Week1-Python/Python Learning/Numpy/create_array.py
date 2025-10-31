import numpy as np

list_1d=[1,2,3,4,5,6]
array_1d=np.array(list_1d)
print(f"Array of 1D is:{array_1d}")

# Length of two sub list should be same for creating a 2d array
list_2d=[[1,2,3,8],[4,5,6,5]]
array_2d=np.array(list_2d)
print(f"Array of 2D is:{array_2d}")

# Shape of Array
print(f"Shape of 1d array:{array_1d.shape}")
print(f"Shape of 2d array:{array_2d.shape}")

# Size
print(f"Size of 1d_array:{array_1d.size}")
print(f"Size of 2d_array:{array_2d.size}")

# Data type of Array
'''
type(array)-> It return the python object type not element datatype
array.dtype->Return datatype of array element 
'''
print(f"Data type of 1d Array is:{type(array_1d)}")
print(f"Data type of 2d Array is:{array_1d.dtype}")

a=[1,2,3,4,5,6]
num=np.array(a)

# Array arrange
array_arrange=np.arange(2,10,2)
print(f"Array arrangement is:{array_arrange}")

#linespace
arry_linespace=np.linspace(1,6,6)
print(f"Array linespace is:{arry_linespace}")

array_ones = np.ones((1, 3))
print("Array of ones:\n", array_ones)

array_zeros = np.zeros((2, 3))
print("Array of zeros:\n", array_zeros)

array_rand=np.random.rand(1,3)
print("Array of rand:\n", array_rand)

array_randn = np.random.randn(2, 3)
print("Random array with randn:\n", array_randn)

array_randint = np.random.randint(0, 10, (2, 3))
print("Random array with randint:\n", array_randint)

'''
Indexing and Slicing
Reshaping Arrays
Change the shape of an array without changing its data using the
 reshape() method.

'''
array = np.array([[1, 2, 3], [4, 5, 6]])

# Indexing
print("Element at [0, 1]:", array[0, 1])
print("Element at [1, 2]:", array[1, 2])

# Slicing
print("First row:", array[0, :])
print("First column:", array[:, 0])
print("Sub-array:", array[0:2, 1:3])

array = np.arange(6)
print("Original array:", array)

reshaped_array = array.reshape((2, 3))
print("Reshaped array:\n", reshaped_array)
