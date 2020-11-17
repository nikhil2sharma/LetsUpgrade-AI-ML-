# Question1
# Given the following jumbled word, OBANWRI guess the correct English word.
# A. RANIBOW
# B. RAINBOW
# C. BOWRANI
# D. ROBWANI

# Solution1
import random
choise_lst=['RANIBOW','RAINBOW','BOWRANI','ROBWANI']
selection=choise_lst[1]
for index,value in enumerate(choise_lst):
    print('Please select index',index,'with value',value)
input1=int(input('Enter the integer index :  '))

if choise_lst[input1]==selection:
    print('You have selected right')
else:
    print('Please chek your selection')


# Question 2.
# Write a program which prints “LETS UPGRADE”. (Please note that you have to
# print in ALL CAPS as given)
input2=input('Enter letsupgrade in any format : ')
print('LETSUPGRADE in all capital ::>>',input2.upper())


###Question3.
# Write a program that takes cost price and selling price as input and displays whether the transaction is a
# Profit or a Loss or Neither.
# INPUT FORMAT
# The first line contains the cost price.
# The second line contains the selling price.
# OUTPUT FORMAT
# Print "Profit" if the transaction is a profit or "Loss" if it is a loss. If it is neither
# profit nor loss, print "Neither". (You must not have quotes in your output)

cost_price=input()
selling_price=input()

if cost_price>selling_price:
    print('Loss')
elif cost_price<selling_price:
    print('Profit')
else:
    print('Neither')


# Question4.
# Write a program that takes an amount in Euros as input. You need to find its equivalent in
# Rupees and display it. Assume 1 Euro equals Rs. 80.
# Please note that you are expected to stick to the given input and output
# format as in sample test cases. Please don't add any extra lines such as
# 'Enter a number', etc.
# Your program should take only one number as input and display the output.

input3=int(input())
in_ruppe=80*input3
print(in_ruppe)




