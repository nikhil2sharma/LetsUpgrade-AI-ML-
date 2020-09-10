#Assignment Solution
#Day-7_08_09_2020
#By  : Nikhil Sharma
#Date_Of_Completion : 10-09-2020


# Question 1:
# Write a program to copy the contents of one file to another using a for loop. (Don’t use built-in copy
# function)

with open('data.txt') as fread:
    with open('data_copy','w+') as fwrite:
        for line in fread:
            fwrite.write(line)

# from shutil import copyfile
# copyfile('data.txt','abc.txt')



# Question 2:
# Write a Python program to find maximum and minimum values in the dictionary. Do not use built-in min
# and max functions.

d={'a':0,'b':-3,'c':150}
max=d['a']
min= d['a']
for value in d.values():
    if max>value:
        pass
    else:
        max=value
    if min<value:
        pass
    else:
        min=value
print('Dictionary max value is:',max,'and min value is :',min)




