#Assignment Solution
#Day-5_07_09_2020
#By  : Nikhil Sharma
#Date_Of_Completion : 08-09-2020


# Question 1 :  Assuming that we have some email addresses in the "username@companyname.com" format,
# please write a program to print the company name of a given email address. Both user names and company
# names are composed of letters only.  Input Format:  The first line of the input contains an email address.
# Output Format:  Print the company name in a single line.
# Example;  Input:  john@google.com Output:  google.

a='john@google.com'
start_index=a.find('@')
output= (a[start_index+1:]).replace('.com','')
print('Output :',output)

# Question 2 :  Write a program that accepts a comma-separated sequence of words as input and
# prints the words in a comma-separated sequence after sorting them alphabetically.
# Input Format:  The first line of input contains words separated by the comma.
# Output Format:  Print the sorted words separated by the comma.
# Example:  Input: without,hello,bag,world  Output:  bag,hello,without,world
input1= ['without','hello','bag','world']
sorted_input=input1.sort()
for elem in sorted(input1):
    print(elem,end=',')



# Question 3: Create your own Jupyter Notebook for Sets. Reference link:
#     https://www.w3schools.com/python/python_sets.asp
'''
Set:
Defination:
    Set is collection of unique sequence(no item is repeated) which is unordered and as it is unordered so 
    it can not be indexing andslicing.

Define : 
Empty set defined : 
set1= set() or placing all the elements within a pair of curly braces

Uses of Set :
You might create an empty set if you eventually want to create a list of unique user input. 
Say, for example, you are creating a form that accepts user input and you want each item that the user enters to be unique. 
In this case, you can create an empty set, go through all the items that the user has entered, and store them in the set. 
Since a set is a collection of unique items, any duplicates are removed. 

Access element of set :
set can access through index value (we can use for and while loop to iterate over).
 
Ex1 
a={1,2,3}
for elem in a:
    print(elem)
    
Various methods of set:
1. add items in the set:
a={1,2}
a.add(3)

2. Finding length of set :
a={1,2,3}
print(len(a))

3. Removeitem from set :(if elem not there remove functionwill raise the error)
print(a.remove(1)) 

Note: If the item to remove does not exist, remove() will raise an error.

4. Remove the item using discard method : (Note it will not raise the error if element not present))
print(a.discard(2))

5. Remove the last item from the set:
print(a.pop())

Note: Sets are unordered, so when using the pop() method, you will not know which item that gets removed.

6. clear method will empty the set
b={1,2,3}
b.clear()

7.delete the set completly

del(a)

Set Operations:
8.Joining the two set :
Using : Union,Update (return type is none,This function will update the value automaticaly)
a={1,2,3}
b={3,4,5}
print(a.union(b))
print(a.update(b))

9. Difference of Sets

The difference operation on two sets produces a new set containing only the 
elements from the first set and none from the second set.

ip1 = set([1,2,3])
ip2 = set([1,2,34,89,4,5,6])
output = ip1 - ip2
print(output)

10. Compare Sets

We can check if a given set is a subset or superset of another set. 
The result is True or False depending on the elements present in the sets.

DaysA = set(["Mon","Tue","Wed"])
DaysB = set(["Mon","Tue","Wed","Thu","Fri","Sat","Sun"])
SubsetRes = DaysA <= DaysB
SupersetRes = DaysB >= DaysA
print(SubsetRes)
print(SupersetRes)


'''
# Question 4:  Given a list of n-1 numbers ranging from 1 to n, your task is to find
# the missing number. There are no duplicates.  Input Format:  The first line contains
# n-1 numbers with each number separated by a space.  Output Format:  Print the missing number
# Example:  Input:  1 2 4 6 3 7 8  Output:  5
# Explanation:  In the above list of numbers 5 is missing and hence 5 is the input

input1 = {1,2, 4, 3, 7, 8}
a=max(input1)
new_ip=set(range(1,a+1))
logic= new_ip-input1
for elem in logic:
    print()
    print(elem)


# Question 5: With a given list L, write a program to print this list L after removing
# all duplicate values with original order reserved.
# Example:  If the input list is  12 24 35 24 88 120 155 88 120 155
# Then the output should be  12 24 35 88 120 155
# Explanation:  Third, the seventh and ninth element of the list L has been removed because
# it was already present.  Input Format:  In one line take the elements of the list L with
# each element separated by a space.  Output Format:  Print the elements of the modified
# list in one line with each element separated by a space.  Example:  Input:  12 24 35 24
# Output:  12 24 35

input1 = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
l=[]

for elem in input1:
    if elem not in l:
        l.append(elem)
for elem in l:
    print(elem,end=' ')




