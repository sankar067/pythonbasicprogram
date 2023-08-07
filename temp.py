# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import constant
    
"""
Keywords in Python programming language

False	class	finally	is	return
None	continue	for	lambda	try
True	def	from	nonlocal	while
and	del	global	not	with
as	elif	if	or	yield
assert	else	import	pass	 
break	except	in	raise	 

Rules for writing identifiers

-Identifiers can be a combination of letters in lowercase (a to z) or uppercase (A to Z) or digits (0 to 9) or an underscore (_). Names like myClass, var_1 and print_this_to_screen, all are valid example.
-An identifier cannot start with a digit. 1variable is invalid, but variable1 is perfectly fine.
-Keywords cannot be used as identifiers.
-We cannot use special symbols like !, @, #, $, % etc. in our identifier.
-Identifier can be of any length.
"""

print("Hello, World!")
"""
invalid identifer
global=1
@=1
"""
""" Multi-line statement
multiple lines with the line continuation character (\).
In Python, line continuation is implied inside parentheses ( ),
 brackets [ ] and braces { }
"""
print('-----Multi statement---------')
a = 1 + 2 + 3 + \
    4 + 5 + 6 + \
    7 + 8 + 9
    
b = (1 + 2 + 3 +
    4 + 5 + 6 +
    7 + 8 + 9)

colors = ['red',
          'blue',
          'green']
""" We could also put multiple statements in a single line using semicolons,as follows"""
x = 1; y = 2; z = 3
""" Python Indentation
 Most of the programming languages like C, C++, Java use braces { } to define a block of code. 
But Python uses indentation

Indentation can be ignored in line continuation. But it's a good idea to always indent. 
It makes the code more readable. For example: check if statement
Incorrect indentation will result into IndentationError
"""
print('-----For and if loop---------')
for i in range(1,11):
     print(i)
     if i==4:
         print('Hello variable continue')
         continue
     # Indentation ignored in below (single line comment) and multiline coment using """ """
     if i==5: print('Hello variable break'); break
""" Docstring in Python
It is a string that occurs as the first statement in a module, function, class, 
or method definition. We must write what a function/class does in the docstring.

Triple quotes are used while writing docstrings. For example:
"""
print('-----Function and docstring---------')
def double(num):
    """Function to double the value"""
    return 2*num
# to print doc string attribute __doc__
print(double.__doc__)
print('-----Variables---------')
#Python Variables, Constants and Literals
#Variable
website = "Apple.com"
print(website)

# assigning a new variable to website
website = "Programiz.com"

print(website)
# Assigning multiple values to multiple variables
print('-----Multiple Variable---------')
a, b, c = 5, 3.2, "hello"
print (a)
print (b)
print (c)
"""Constants-A constant is a type of variable whose value cannot be changed.
Assigning value to a constant in Python-
constants are usually declared and assigned on a module. Here, the module means a new file containing variables, 
functions etc which is imported to main file(constant.py).
Inside the module, constants are written in all capital letters and underscores separating the words.
"""
print('-----Constansts from Constant module---------')
print(constant.PI)
print(constant.GRAVITY)
""" Rules and Naming convention for variables and constants
-Create a name that makes sense. Suppose, vowel makes more sense than v.
-Use camelCase notation to declare a variable. It starts with lowercase letter.
 For example:
myName
myAge
myAddress
-Use capital letters where possible to declare a constant. For example:
PI
G
MASS
TEMP
-Never use special symbols like !, @, #, $, %, etc.
-Don't start name with a digit.
-Constants are put into Python modules and meant not be changed.
-Constant and variable names should have combination of letters in lowercase (a to z) or uppercase (A to Z) or digits (0 to 9) or an underscore (_). 
For example:
snake_case
MACRO_CASE
camelCase
CapWords
"""
print('------Naming convention for variables and constants--------')
myName='sankar'
CapWords={"A","B"}
"""Numeric Literals
Numeric Literals are immutable (unchangeable). Numeric literals can belong to 3 different 
numerical types Integer, Float and Complex.
How to use Numeric literals in Python? For Example:
"""
print('-----Numeric Literals---------')
aa = 0b1010 #Binary Literals
bb = 100 #Decimal Literal 
cc = 0o310 #Octal Literal
dd = 0x12c #Hexadecimal Literal

#Float Literal
float_1 = 10.5 
float_2 = 1.5e2

#Complex Literal 
x = 3.14j

print(aa,bb,cc,dd)
print(float_1, float_2)
print(x, x.imag, x.real)
"""String literals
A string literal is a sequence of characters surrounded by quotes.
We can use both single, double or triple quotes for a string. And, a character literal is a single character surrounded by single or double quotes.
"""
print('-----String literals---------')
strings = "This is Python"
char = "C"
multiline_str = """This is a multiline string with more than one line code."""
unicode = u"\u00dcnic\u00f6de"
raw_str = r"raw \n string"

print(strings)
print(char)
print(multiline_str)
print(unicode)
print(raw_str)
"""Boolean literals
A Boolean literal can have any of the two values: True or False.
In Python, True represents the value as 1 and False as 0."""
print('-----Boolean literals---------')
x = (1 == True)
y = (1 == False)
a = True + 4
b = False + 10

print("x is", x)
print("y is", y)
print("a:", a)
print("b:", b)
"""Special literals
Python contains one special literal i.e. None. We use it to specify to that field that is not created.
 we define a menu function. Inside menu, when we set parameter as drink then, it displays Available. 
 And, when the parameter is food, it displays None"""
print('-----Special literals---------')
drink = "Available"
food = None

def menu(x):
    if x == drink:
        print(drink)
    else:
        print(food)

menu(drink)
menu(food)
"""Literal Collections
There are four different literal collections List literals, Tuple literals, Dict literals, and Set literals.
List is an ordered sequence of items. It is one of the most used datatype in Python and is very flexible
Tuples once created cannot be modified.
Dictionary is an unordered collection of key-value pairs.
Items in a set are not ordered
"""
fruits = ["apple", "mango", "orange"] #list
numbers = (1, 2, 3) #tuple
alphabets = {'a':'apple', 'b':'ball', 'c':'cat'} #dictionary
vowels = {'a', 'e', 'i' , 'o', 'u'} #set

print(fruits)
print(numbers)
print(alphabets)
print(vowels)
#Lists are mutable, meaning, value of elements of a list can be altered.
ac = [5,10,15,20,25,30,35,40]
# a[2] = 15
print("ac[2] = ", ac[2])

# a[0:3] = [5, 10, 15]
print("ac[0:3] = ", ac[0:3])

# a[5:] = [30, 35, 40]
print("ac[5:] = ", ac[5:])
#Tuple:We can use the slicing operator [] to extract items but we cannot change its value.
t = (5,'program', 1+3j)

# t[1] = 'program'
print("t[1] = ", t[1])

# t[0:3] = (5, 'program', (1+3j))
print("t[0:3] = ", t[0:3])

# Generates error
# Tuples are immutable
try:
    t[0] = 10
except TypeError:
    print('tuple object does not support item assignment')
"""Python Strings
String is sequence of Unicode characters. We can use single quotes or double quotes to represent strings. 
Multi-line strings can be denoted using triple quotes either 3 single(') or 3 double quote(")
"""    
s = 'Hello world!'

# s[4] = 'o'
print("s[4] = ", s[4])

# s[6:11] = 'world'
print("s[6:11] = ", s[6:11])

# Generates error
# Strings are immutable in Python
try:
    s[5] ='d'
except TypeError:
    print('str object does not support item assignment')
"""Python Set
Set is an unordered collection of unique items. 
Set is defined by values separated by comma inside braces { }. Items in a set are not ordered.
We can perform set operations like union, intersection on two sets. 
Set have unique values. They eliminate duplicates.
"""
abc = {5,2,3,1,4}

# printing set variable
print("abc = ", abc)

# data type of variable a
print(type(abc))

""" For below slicing oprator for python set will give error
Traceback (most recent call last):

  File "<ipython-input-43-c8d41375bc2e>", line 1, in <module>
  File sitecustomize.py, line 705, in runfile
    execfile(filename, namespace)
  File sitecustomize.py, line 102, in execfile
    exec(compile(f.read(), filename, 'exec'), namespace)
  File temp.py, line 272, in <module>
    print(a[1])
TypeError: 'int' object is not subscriptable
"""
#print(a[1])

"""Python Dictionary
Dictionary is an unordered collection of key-value pairs.
It is generally used when we have a huge amount of data. Dictionaries are optimized for retrieving data. We must know the key to retrieve the value.
In Python, dictionaries are defined within braces {} with each item being a pair in the form key:value. Key and value can be of any type.

"""
d = {1:'value','key':2}
print(type(d))

print("d[1] = ", d[1]);

print("d['key'] = ", d['key']);

# Generates error as We use key to retrieve the respective value. But not the other way around.
#print("d[2] = ", d[2]);
"""Conversion between data types
We can convert between different data types by using different type conversion functions like int(), float(), str() etc.

Conversion from float to int will truncate the value (make it closer to zero).
"""
print(int(10.6))
print(int(-10.6))
print(float(5))
print(float('2.5'))
print(str(25))
#print(int('1p'))#Conversion to and from string must contain compatible values.
#We can even convert one sequence to another.
print(set([1,2,3]))
print(tuple({5,6,7}))
print(list('hello'))
#To convert to dictionary, each element must be a pair
print(dict([[1,2],[3,4]]))