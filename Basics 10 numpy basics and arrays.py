# -*- coding: utf-8 -*-

#### NUMPY basics and 1D numpy arrays


import numpy as np
import matplotlib.pyplot as plt # (Used only at the end for sine graph)


#Make a numpy array

#Numpy arrays are usually fixed in size and data of the same type
#They can also be used as vectors

a = np.array([0, 1, 2, 3, 4,])

#type(a) just returns "class numpy.ndarray"
#To get the actual data type use [variable name].dtype
print("Array 'a' has data type: ", a.dtype)
print(a.size) # Returns number of elements
print(a.shape) # Returns tuple of the size of the array in multiple dimensions
print(a.ndim) # Number of dimensions



#Manipulating arrays

c = np.array([20, 1, 2, 3, 4])
print(c)
#Change an element's value
c[0] = 100
c[3:5] = 300, 400
print(c)
#copy part of it to a new array
d = c[1:4]
print(d)



#Basic Operations (Vector addition etc. take much less code in Numpy)
print("")



u = np.array([1, 0])
v = np.array([0, 1])
print("u: ", u)
print("v: ", v)

z1 = u + v
z2 = u - v
z3 = 2*u
z4 = np.dot(u, v) # Dot product
z5 = u + 1 # Adding a constant

print("z1: ", z1, "z2: ", z2, "z3: ", z3, "z4: ", z4, "z5: ", z5)



# Universal functions
print("")

#Note: in numpy, the number Pi is "np.pi"
a = np.array([1, -1, 1, -1])
print(a)

a_mean = a.mean()
print(a_mean)
a_biggest_value = a.max()
print(a_biggest_value)



#Let's make a Sine graph!
print("")

#First let's just try some basic math
x = np.array([0, np.pi/2, np.pi])
y = np.sin(x)
print(x)
print(y)

#Ok, now lets use numpy.linspace to make loads of steps
x = np.linspace(0, 2*np.pi, 100) # Start, stop, number of steps
y = np.sin(x)
plt.plot(x, y)



