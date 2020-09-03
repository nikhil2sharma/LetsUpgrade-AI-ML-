#Assignment Solution
#Day-3_2nd_09_2020
#By  : Nikhil Sharma
#Date_Of_Completion : 03-09-2020


# Question 1:
# Write a program to subtract two complex numbers in Python.
a=2+3j
b=1+2j
sub_result = a-b
print('Substraction result for two complex numbers is : ',sub_result)



# Question 2 :
# Write a program to find the fourth root of a number.
num = 16
fourth_root= num**(1/4)
print('Fourth root of the number is :',fourth_root)



# Question 3:
# Write a program to swap two numbers in Python with the help of a temporary variable.
a=2
b=4
sum=a+b
b=sum-b
a=sum-a

print('Printing Swap Number using temp var : ',a,b)




# Question 4:
# Write a program to swap two numbers in Python without using a temporary variable.
a=2
b=4
a,b=b,a
print('Printing Swap Number using temp var : ',a,b)





# Question 5:
# Write a program to convert Fahrenheit to kelvin and celsius both.
farh_value=10

kelvin_value = 273.5+((farh_value-32)*(5.0/9.0))
celsius_value = ((farh_value-32)*(5.0/9.0))
print('Kelvin value for 10 Fahrenheit ',kelvin_value)
print('Celsius Value for 10 Fahrenheit',celsius_value)




# Question 6:
# Write a program to demonstrate all the available data types in Python. Hint: Use type() function.
int_num=1
float_num=2.0
complex_num=1+2j
string_num='johny'
bool_num=True
list_num=[1,2]
tuple_num=(1,2)
dict_num={'a':1}

print('int_Datatype',type(int_num))
print('float_Datatype',type(float_num))
print('complex_Datatype',type(complex_num))
print('string_Datatype',type(string_num))
print('bool_Datatype',type(bool_num))
print('list_Datatype',type(list_num))
print('tuple_Datatype',type(tuple_num))
print('dict_Datatype',type(dict_num))













