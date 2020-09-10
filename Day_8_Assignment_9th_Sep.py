#Assignment Solution
#Day-8_09_09_2020
#By  : Nikhil Sharma
#Date_Of_Completion : 10-09-2020

# Question
# 1:Recreate “NB21 map, filter, lambda.ipynb” to try different variations or
# perform different calculations from the ones that are in the NB

# The map() is a function that takes in two arguments:
#
# A function
# A sequence iterable.
# In the form: map(function, sequence)
#
# The first argument is the name of a function and the second a sequence (e.g. a list). map()
# applies the function to all the elements of the sequence. It returns a new list with the elements
# changed by the function.

def fahrenheit(T):
    return ((float(9)/5)*T + 32)


def celsius(T):
    return (float(5)/9)*(T-32)

temp = [0, 22.5, 40,100]

# l1 = []
# for i in temp:
#     l1.append(fahrenheit(i))
# print(l1)

print(list(map(lambda x :(((9)/5)*x + 32), temp)))

# Map is more commonly used with lambda expressions since the entire purpose of a map()
# is to save effort on creating manual for loops.

# map() can be applied to more than one iterable. The iterables must have the same length.
#
# For instance, if we are working with two lists-map() will apply its lambda function to the elements
# of the argument lists, i.e. it first applies to the elements with the 0th index, then to the elements
# with the 1st index until the nth index is reached.

# For example, let's map a lambda expression to two lists:

a = [1,2,3,4]
b = [5,6,7,8]
c = [9,10,11,12,4,5]
print(list(map(lambda x,y : x+y , a,b)))
def sum(x,y,z):
    return x+y+z

# Now all three lists
print(list(map(sum, a,b,c)))


##Reduce Function:
# The function reduce(function, sequence) continually applies the function to the sequence. It then returns
# a single value.
#
# If seq = [s1, s2, s3, ... , sn], calling reduce(function, sequence) works like this:
#
# At first the first two elements of sequence will be applied to function, i.e. func(s1,s2)
# The list on which reduce() works looks like this: [ function(s1, s2), s3, ... , sn ]
# In the next step the function will be applied on the previous result and the third element of the list, i.e. function(function(s1, s2),s3)
# The list looks like: [ function(function(s1, s2),s3), ... , sn ]
# It continues like this until just one element is left and return this element as the result of reduce()


from functools import reduce
lst =['sdfs','sdfsfsdf','sdf']
print(reduce(lambda a,b:a+b,lst))

max_find = lambda a,b:a if a>b else b
lst=[47,11,42,13]

#find max
print(reduce(max_find,lst))


#Filter
# The function filter(function, list) offers a convenient way to filter out all the elements
# of an iterable, for which the function returns "True".
#
# The function filter(function(),l) needs a function as its first argument. The function
# needs to return a Boolean value (either True or False). This function will be applied to
# every element of the iterable. Only if the function returns "True" will the element of the
# iterable be included in the result.
#
#First let's make a function
def odd_check(num):
    if num%2 !=0:
        return True

lst =[1,2,3,4,5,6,7,8]

print(list(filter(odd_check,lst)))

# With lambda function
print(list(map(lambda x: x%2!=0,lst)))



#Python Lambda

# lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.

# Syntax:
# lambda arguments : expression
# The expression is executed and the result is returned:

# A lambda function that adds 10 to the number passed in as an argument, and print the result:
x = lambda a : a + 10
print(x(5))

# Note :Use lambda functions when an anonymous function is required for a short period of time.


# Question 2: Recreate your own Python NB
# for “Classes and Objects” from the pdf provided namely “Classes & Objects.pdf”

# Object Oriented Programming and File I/O

# Object Oriented Programming (OOP) is a programming paradigm that allows abstraction through the
# concept of interacting entities. This programming works contradictory to conventional model and
# is procedural, in which programs are organized as a sequence of commands or statements to perform.
#
# We can think an object as an entity that resides in memory, has a state and it's able to perform some actions.
#
# More formally objects are entities that represent instances of a general abstract concept called class.
# In Python, "attributes" are the variables defining an object state and the possible actions are called
# "methods".
# In Python, everything is an object also classes and functions.
# Class names should always be uppercase (it's a naming convention).

class P:
    pass


a=P()
# Here 'a' is an instance of a class.
a.name='Sai'
a.surname='Kiran'
a.yob=1998
print("%s %s was born in %d." %(a.name, a.surname, a.yob))
print(a)


#More professional way in writing the class is :
class CAR:
    def __init__(self,model_name,model_make):
        self.mname=model_name
        self.mmake=model_make

#__init__ it is a constructor __init__(self, ...)
# Is a special _Python_ method that is automatically called after an object construction.
# Its purpose is to initialize every object state. The first argument
# (by convention) __self__ is automatically passed either and refers to the object itself.
# We cannot directly manipulate any class rather we need to create an instance of the class:

### 1.2 Methods
class PERSON:
    def __init__(self,name,surname,yob):
        self.nm=name
        self.sname=surname
        self.yob=yob

        def age(a,current_year):
            print(current_year-self.yob)

        def __str__(self):
            return "%s %s was born in %d ." % (self.nm, self.sname, self.yob)


sai = PERSON("Sai", "Kiran", 1998)
print(sai)
print(sai.age(2020))







