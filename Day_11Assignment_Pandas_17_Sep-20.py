#Assignment Solution
#Day-10_11_09_2020
#By  : Nikhil Sharma
#Date_Of_Completion : 15-09-2020

# Question 1:
# Create an element-wise comparison (greater, greater_equal, less and less_equal) of two given arrays

import numpy as np
import pandas as pd
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



# Question 6:
# Write a Pandas program to create and display a DataFrame from a specified dictionary data which has the
# index labels

dict1={'Name':['Arindam','Sai','Johny'],'Age':[20,30,40],'Salary':[100,200,300]}
dict_dataframe=pd.DataFrame(dict1)
print(dict_dataframe)


# Question 7:
# Write a Pandas program to select the 'name' and 'score' columns from the following DataFrame.
#Here I will consider iris dataset
iris_data=pd.read_csv(r'C:\Users\nikhisha\Letsupgrade\Python\iris_dataset.csv')
print(iris_data.head())
print('Printing two columns of pandas ')
# print(iris_data.loc[:4,['species','petal_length']])
print(iris_data.iloc[:3,1:3])
# print(iris_data.ix[:4,['species','petal_length']])


# Question 8:
# Write a Pandas program to join the two given dataframes along rows and assign all data.

left = pd.DataFrame({'Sr.no': ['1', '2', '3', '4', '5'],
                     'Name': ['Rashmi', 'Arun', 'John',
                              'Kshitu', 'Bresha'],
                     'Roll No': ['1', '2', '3', '4', '5']})

right = pd.DataFrame({'Srn': ['2', '4', '6', '7', '8'],
                      'Gender': ['F', 'M', 'M', 'F', 'F'],
                      'Interest': ['Writing', 'Cricket', 'Dancing',
                                   'Chess', 'Sleeping']})

print(left.head())
print(right.head())
# print('Merge Result column wise')
# #inner
# print('Inner join')
# print(pd.merge(left,right,how='inner',left_on='Sr.no',right_on='Srn'))
# #outter
# print('Outter Join')
# print(pd.merge(left,right,how='outer',left_on='Sr.no',right_on='Srn'))
# print('Left Join')
# print(pd.merge(left,right,how='left',left_on='Sr.no',right_on='Srn'))
# print('Right Join')
# print(pd.merge(left,right,how='right',left_on='Sr.no',right_on='Srn'))

print('Pandas program to join the two given dataframes along rows')
print(pd.concat([left,right]))


# Question 9:
# Write a Pandas program to detect missing values of a given DataFrame. Display True or False.
data=pd.concat([left,right])
print('Printing False for missing value and True for having a value')
print(data.isnull())

# Question 10:
# Write a Pandas program to create and display a one-dimensional array-like object containing an array of
# data.
one_dim_data=pd.Series([1,2,3,4,5])
print('One dimension data using Pandas')
print(one_dim_data)




