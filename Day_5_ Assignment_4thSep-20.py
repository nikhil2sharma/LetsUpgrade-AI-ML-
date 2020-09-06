


# Question 1 :
# Write a Python program to find the first 20 non-even prime natural numbers.
lower = 1
upper = 100
cnt=1
print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           cnt+=1
           print(num)
           if cnt==21:
               break


# Question 2 :
# Write a Python program to implement 15 functions of string.


str = "journey Toward AI-ML."

# 1 Python String capitalize() Method > Make first letter capital rest convert in lower case
print(str.capitalize())
# 2 Python String casefold() Method >Make the string lower case:
print(str.casefold())
# 3 Python String center() Method >Print the str "journey Toward AI-ML.", taking up the space of 100 characters, with "banana" in the middle:
print(str.center(100))
# 4 Python String count() Method >Return the number of times the value "o" appears in the string:
print(str.count('o'))

# 5 Python String encode() Method >UTF-8 encode the string:
print(str.encode('UTF-8')) #by default utf-8

# 6 Python String endswith() Method >Check if the string ends with a punctuation sign (.):

print(str.endswith('.'))

# 7 Python String expandtabs() Method >Set the tab size to 50 whitespaces:
str1='he\tllo'
print(str1.expandtabs(50))


#8 Python String find() Method > Where in the text is the word "Toward"?:
print(str.find('Toward'))


# 9 Python String format() Method >>#Use "b" to convert the number into binary format:

str2 = "The binary version of {0} is {0:b}"
print(str2.format(2))

# 10 Python String index() Method > Where in the text is the word "Toward"?:
print(str.index('Toward'))


# Question 3:
# Write a Python program to check if the given string is a Palindrome or Anagram or None of them. Display
# the message accordingly to the user.
a='radar'
b='adarr'
list_a=list(a)
list_b=list(b)

#Checking Palindrome
if (a[:]== a[::-1]):
    print('Palindrome')
#Checking Anagram
if list_a.sort() == list_b.sort():
    print('Anagram')
#Else None
else:
    print('None of them')




# Question 4:
# Write a Python's user-defined function that removes all the additional characters from the string and
# convert it finally to lower case using built-in lower(). eg: If the string is "Dr. Darshan Ingle @AIML Trainer",
# then the output be "drdarshaningleaimltrainer".

s= 'Dr. Darshan Ingle @AIML Trainer'
s_change=''.join(s.replace('.','').replace('@','').split())
print(s_change.lower())




















