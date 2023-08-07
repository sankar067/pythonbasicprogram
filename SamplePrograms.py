# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 17:24:55 2018

@author: SANKAR
"""

def addTwonumbers(num1,num2):
    """ Program addition of 2 number based on parameters\n"""
    # Add two numbers
    sum = float(num1) + float(num2)
    # Display the sum
    print('The sum of {0} and {1} is {2}\n'.format(num1, num2, sum))
    return sum
#
#def addTwonumbers2():
#    """ Program addition of 2 number based user input\n"""
#    num1 = input('Enter first number: ')
#    num2 = input('Enter second number: ')
#    # Add two numbers
#    sum = float(num1) + float(num2)
#    # Display the sum
#    print('The sum of {0} and {1} is {2}\n'.format(num1, num2, sum))

def findLargestNumber(num1,num2,num3):
    """Python program to find the largest number among the three input numbers \n"""

    # uncomment following lines to take three numbers from user
    #num1 = float(input("Enter first number: "))
    #num2 = float(input("Enter second number: "))
    #num3 = float(input("Enter third number: "))
    
    if (num1 >= num2) and (num1 >= num3):
       largest = num1
    elif (num2 >= num1) and (num2 >= num3):
       largest = num2
    else:
       largest = num3
    
    print("The largest number between",num1,",",num2,"and",num3,"is",largest)

# Python Program to find the L.C.M. of two input number 
"""The least common multiple (L.C.M.) of two numbers is the smallest positive integer 
that is perfectly divisible by the two given numbers.
For example, the L.C.M. of 12 and 14 is 84.
"""
def findLCMofTwoNumber(x,y):

   """This function takes two
   integers and returns the L.C.M."""

   # choose the greater number
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm

# Python program to find the L.C.M. of two input number
# define gcd function
def gcd(x, y):
   """This function implements the Euclidian algorithm
   to find G.C.D. of two numbers"""

   while(y):
       x, y = y, x % y

   return x

# define lcm function
def lcm(x, y):
   """This function takes two
   integers and returns the L.C.M."""

   lcm = (x*y)//gcd(x,y)
   return lcm

# Python Program to calculate the square root of real numbers
def squarerootRealNumber(Num):
    """ Program to calculate the square root of real numbers """
    num_sqrt = Num ** 0.5
    print('The square root of %0.3f is %0.3f'%(Num ,num_sqrt))

print(addTwonumbers.__doc__)
addTwonumbers(1.5,6.3)
#
#print(addTwonumbers2.__doc__)
#addTwonumbers2()

print(findLargestNumber.__doc__)
findLargestNumber(11,55,22)

print(findLCMofTwoNumber.__doc__)
print("The L.C.M. of {0} and {1} is", findLCMofTwoNumber(54, 24))

print(lcm.__doc__)
print("The LCM of 2 No. is", lcm(12, 14))

print(gcd.__doc__)
print("The GCD of 2 Nos is", gcd(54, 24))

print(squarerootRealNumber.__doc__)
squarerootRealNumber(8)