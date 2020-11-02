# array in python
# there are six  ways to create array
# array(), linspace(), logspace(), arange(), zeros(), ones()
# 1. array()
from numpy import *

arr = array([1, 2, 3, 4])
print(arr)
print(arr.dtype)

arr = array([1, 2.2, 3, 4.6])
print(arr)
print(arr.dtype)
# it detect data type we don't need to declare
# we can explicitly mention data type inside array
arr = array([1, 2, 3, 4, 5], int)
print(arr)
print(arr.dtype)
arr = array([1, 2, 3, 4, 5], float)
print(arr)
print(arr.dtype)

# 2. linspace()
arr = linspace(0, 10, 11)  # 0 starts 10 end value 11 parts
print(arr)
arr = linspace(0, 10, 5)
print(arr)
arr = linspace(0, 10)  # it will print 50 elements of parts
print(arr)

# 3. logspace()
arr = logspace(0, 10, 5)  # it generate log base value with number of parts of 5
print(arr)

# 4. arange()
arr = arange(0, 10, 2)  # 0 starting number and 10 ending number 2 is step or increment or decrement value
print(arr)
arr = arange(0, 10)  # it steps default one
print(arr)
arr = arange(10, 0, -2)
print(arr)

# 5. zeros()
arr = zeros(10)  # create array of zero filled size of 10
print(arr)
arr = zeros(10, int)
print(arr)

# 6. ones()
arr = ones(10)  # create array of ones filled size of 10
print(arr)
arr = ones(10, int)
print(arr)

# array operations
arr1 = array([1, 2, 3, 4])
print(arr1 + 2)  # adding 2 to each elements

arr2 = array([5, 6, 7, 8])
print(arr1 + arr2)  # this is called vector based operation and suitable for vector operations
print(concatenate([arr1, arr2]))  # concatenate arrays

arr = array([1, 2, 3, 4])
print(sin(arr))  # sin
print(cos(arr))  # cos
print(tan(arr))  # tan
print(log10(arr))  # log10
print(log(arr))  # log
print(sqrt(arr))  # square root
print(cbrt(arr))  # cube root
print(sum(arr))  # sum of all elements
print(min(arr))  # minimum value of array
print(max(arr))  # maximum value of array

# array aliasing and array copy
arr1 = array([1, 2, 3, 4])
arr2 = arr1
print(arr1)
print(arr2)
print(id(arr1))
print(id(arr2))  # both array shares same memory location this is aliasong and not proper array copy

# array shallow copy
# this will affects value when change in one array
arr2 = arr1.view()  # copies arr1 to arr2 with separate memory location
print(arr1)
print(arr2)
arr1[2] = 0
print(arr1)
print(arr2)  # affects another array as well this is shallow copy there is link
print(id(arr1))
print(id(arr2))

# array deep copy
# this will not affect value when changing in another array
arr2 = arr1.copy()
print(arr1)
print(arr2)
arr1[2] = 3
print(arr1)
print(arr2)

# two dimensional array
arr = array([[1, 2], [3, 4]])
print(arr)
print(arr.ndim)  # gives no.of dimension
print(arr.shape)  # gives no.of rows and columns
print(arr.size)  # gives size of array
arr1 = arr.flatten()  # converts multi dimensional array to 1d array
print(arr1)
arr1 = arr1.reshape(2, 2)  # converts 1d array multi dimensional array
print(arr1)

# matrix
arr = array([[1, 2, 3, 4], [5, 6, 7, 8]])
mat = matrix('1, 2, 3, 4; 5, 6, 7, 8')  # converts to array
mat = matrix('1, 2; 3, 4; 5, 6; 7, 8')  # converts to array ; is mentions new row
print(mat)
mat = matrix(arr)  # converts array to matrix to perform matrix based operations
print(mat)
print(diagonal(mat))  # prints diagonal elements
print(mat.min())  # minimum value of matrix
print(mat.max())  # maximum value of matrix
mat1 = matrix('1, 2, 3; 4, 5, 6').reshape(2, 3)
mat2 = matrix('7, 8, 9; 2, 4, 6').reshape(2, 3)
print(mat1 + mat2)  # matrix addition
print(mat1 - mat2)  # matrix subtraction
print(mat1 * mat2)  # matrix multiplication
print(mat1 / mat2)  # matrix division
