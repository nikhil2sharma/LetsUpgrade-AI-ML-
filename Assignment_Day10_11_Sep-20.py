#Assignment Solution
#Day-10_11_09_2020
#By  : Nikhil Sharma
#Date_Of_Completion : 15-09-2020

# Question 1:
# Create an element-wise comparison (greater, greater_equal, less and less_equal) of two given arrays

import numpy as np

array1=np.array([1,2,3,4,5])
array2=np.array([3,4,5,6,6])
array3=np.array([[1,2,3],[3,4,5]])
array4=np.array([[5,6,7],[8,9,2]])

# greater
# print(array1>array2)
# print(array3>array4)
#
# print(array1>array2)
# print(array3>array4)


print(np.greater(array1,array2))
print(np.greater(array3,array4))

# greater_equal
# print(array1>=array2)
# print(array3>=array4)

print(np.greater_equal(array1,array2))
print(np.greater_equal(array3,array4))



# less
print(array1<array2)
print(array3<array4)



print(np.less(array1,array2))
print(array3<array4)
# less_equal
print(array1<=array2)
print(array3<=array4)

print(array1<=array2)
# print(array3<=array4)
print(np.less_equal(array3,array4))


# Question 2:
# Write a NumPy program to create an array of 10 zeros,10 ones, 10 fives

print(np.zeros(10))
print(np.ones(10))
print(np.full(10,5))


# Question 3:
# Write a NumPy program to compute sum of all elements, sum of each column and sum of each row of a
# given array

a=np.array([[1,2,3],[1,2,3]])

print('sum of all elements',np.sum(a))
print('sum of each column',np.sum(a,axis=0))
print('sum of each row',np.sum(a,axis=1))




# Question 4:
# Write a NumPy program to add, subtract, multiply, divide arguments element-wise
a= np.array([1,2,3])
b= np.array([4,5,6])

print('Add result using Numpy Program',np.add(a,b))
print('Sub result using Numpy Program',np.subtract(a,b))
print('Multiply result using Numpy Program',np.multiply(a,b))
print('Divide result using Numpy Program',np.divide(a,b))



# Question 5:
# Write a NumPy program to compute the trigonometric sine, cosine and tangent array of angles given in
# degree.
angles=np.array([30,60,90,120,180])

print('sine value for degree',np.sin(angles))
print('cosine value for degree',np.cos(angles))
print('tan value for degree',np.tan(angles))



