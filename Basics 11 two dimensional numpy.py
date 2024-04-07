# -*- coding: utf-8 -*-

#### 2 Dimensional numpy basics,
import numpy as np
print("#####################")
print("")


#Making a 2D array

#Imagine the following nested list.
a = [[11, 12, 13], [21, 22, 23], [31, 32, 33]]
#It can be passed into numpy and imagined as a matrix
#(Could also have been directly typed into numpy function)
A = np.array(a)
print(A)
print("Dimensions: ", A.ndim)
print("Shape: ", A.shape)
print("Size (elements): ", A.size)
print("A[1][1]: ", A[1][1])
print("A[0, 0:2]: ", A[0, 0:2])
#The first index in "shape"; the first "axis", refers to the number of rows (or nested lists)
#Same applies to selecting elements;

#A[0][1] is the first list/row, second element/column (in this case the number 12)
#A[0, 0:2] means -> first list(/row) -> first 2 elements of that row



#Basic operations
print("")

x = np.array([[1, 0], [0, 1]])
print("X")
print(x)

y = np.array([[2, 1], [1, 2]])
print("Y")
print(y)


z_add = x + y
print("Added:")
print(z_add)

z_scale = 2 * y
print("2Y:")
print(z_scale)

#Regular matrix multiplication
#Recall that matrix mult. involves summing the product
# of elements in the ith row and jth column
z_mult = np.dot(x,y)
print("Matrix multiplication:")
print(z_mult)


#Element-wise mult. or "Hadamard" product
z_elementwisemult = x * y
print("Hadamard (Element-wise) multiplication:")
print(z_elementwisemult)


