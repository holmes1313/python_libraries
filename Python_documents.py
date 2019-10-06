# -*- coding: utf-8 -*-

# The Python Tutorial

# 3.1.2. Strings
'''
If you don’t want characters prefaced by \ to be interpreted as special characters, you can use raw strings by adding an r before the first quote:'''
print('C:\some\name')
print('C:\some\\name')
print(r'C:\some\name')

file = open(r'C:\Users\z.chen7\Downloads\Python\hamlet.txt').read()
file

'''
Python strings cannot be changed — they are immutable. Therefore, assigning to an indexed position in the string results in an error.'''


# String Methods
'''
str.zfill(width)
Return a copy of the string left filled with ASCII '0' digits to make a string of length width. 
A leading sign prefix ('+'/'-') is handled by inserting the padding after the sign character rather than before. 
The original string is returned if width is less than or equal to len(s).'''
'42'.zfill(5)
'-43'.zfill(5)
'43.d'.zfill(5)


# 3.1.3 Lists
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# clear the list by replacing all the elements with an empty list
letters[:] = []
letters

# Fibonacci series:
# the sum of two elements defines the next
a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a+b
    

# 4.3 the range() function
print(range(10))
'''
In many ways the object returned by range() behaves 
as if it is a list, but in fact it isn’t. 
It is an object which returns the successive items 
of the desired sequence when you iterate over it, 
but it doesn’t really make the list, thus saving space.

We say such an object is iterable, that is, 
suitable as a target for functions and constructs 
that expect something from which they can obtain 
successive items until the supply is exhausted. 
We have seen that the for statement is such an 
iterator. The function list() is another; 
it creates lists from iterables:'''
list(range(10))


# 4.4. break and continue Statements, and else Clauses on Loops
'''
The break statement, like in C, breaks out of the 
innermost enclosing for or while loop.'''
for n in range(2, 10):
    for x in range(2, n):
        print(n, '%', x, '=', n%x)
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')
'''      
When used with a loop, the else clause has more 
in common with the else clause of a try statement 
than it does that of if statements: 
    a try statement’s else clause runs when 
    no exception occurs, and a loop’s else clause 
    runs when no break occurs.'''
    
'''
The continue statement, also borrowed from C, 
continues with the next iteration of the loop:'''
for num in range(2, 10):
    if num % 2 == 0:
        print('Found an even number', num)
        continue
    print('Found a number', num)


# 4.6 Defining functions
def fib(n):
    """Print a Fibonacci series up to n"""   # docstring
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

fib(2000)

'''
A function definition introduces the function 
name in the current symbol table. The value of the 
function name has a type that is recognized by the 
interpreter as a user-defined function. This value 
can be assigned to another name which can then also 
be used as a function.'''
fib
f = fib
f(100)

'''
In fact, even functions without a return statement 
do return a value, albeit a rather boring one. 
This value is called None (it’s a built-in name). 
Writing the value None is normally suppressed by 
the interpreter if it would be the only value written.'''
print(fib(0))

def fib2(n):
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

f100 = fib2(100)
f100
'''
The return statement returns with a value from a function. 
return without an expression argument returns None. 
Falling off the end of a function also returns None.'''


# 4.7 More on Defining Functions

"""
argument:
A value passed to a function (or method) when calling the function.
There are two kinds of arguments:
    1. keyword argument:
        complex(real=3, imag=5)
        complex(**{'real': 3, 'imag': 5})
    2. positional argument:
        complex(3, 5),
        complex(*(3, 5))
"""

"""
When a final formal parameter of the form 
**name is present, it receives a dictionary 
containing all keyword arguments except for those 
corresponding to a formal parameter. 
This may be combined with a formal parameter of 
the form *name which receives a tuple containing 
the positional arguments beyond the formal parameter 
list. (*name must occur before **name.) """
def cheeseshop(kind, *args, **kargs):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we are all out of", kind)
    for arg in args:
        print(arg)
    print("-" * 40)
    for key, val in kargs.items():
        print(key, ":", val)

cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")

cheeseshop("Limburger", 
           *["It's very runny, sir.", 
             "It's really very, VERY runny, sir."],
           **{'shopkeeper': "Michael Palin",
              'client': "John Cleese",
              'sketch': "Cheese Shop Sketch"})

# 4.7.4 Unpacking argument lists
'''
The reverse situation occurs when the arguments 
are already in a list or tuple but need to be unpacked 
for a function call requiring separate positional arguments.'''
list(range(3, 6))
args = [3, 6]
list(range(args))   # TypeError
list(range(*args))
'''
In the same fashion, dictionaries can deliver 
keyword arguments with the ** operator:'''
def parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")

d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot(**d)


"""
Don’t use fancy encodings if your code is meant 
to be used in international environments. 
Python’s default, UTF-8, or even plain ASCII work 
best in any case."""


# 5.1. More on Lists¶
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.count('apple')
fruits.index('banana')
fruits.index('banana', 4)  # find next banana starting a position 4
fruits.reverse()
fruits
fruits.append('grape')
fruits
fruits.sort()
fruits
fruits.pop()

'''
Stack is a linear data structure which follows a particular order in which the 
operations are performed. The order may be LIFO(Last In First Out) or FILO(First In Last Out).'''

'''
It is also possible to use a list as a queue, where the first element added is 
the first element retrieved (“first-in, first-out”); however, lists are not 
efficient for this purpose. While appends and pops from the end of list are fast, 
doing inserts or pops from the beginning of a list is slow (because all of the 
other elements have to be shifted by one).

To implement a queue, use collections.deque which was designed to have fast 
appends and pops from both ends. For example:'''
from collections import deque
queue = deque(['Eric', 'John', 'Michael'])
queue.append('Terry')
queue.append('Graham')
queue
queue.popleft()
queue.popleft()
queue

# 5.1.3 List comprehensions
list(map(lambda x: x**2, range(10)))

[x**2 for x in range(10) if x % 2 == 0]

[(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]

# the tuple must be parenthesized, otherwise an error is raised
[x, x**2 for x in range(6)]

# flatten a list using a listcomp with two 'for'
vec = [[1,2,3], [4,5,6], [7,8,9]]
[num for elem in vec for num in elem]

from math import pi
pi
[str(round(pi, i)) for i in range(1, 6)]


matrix = [     
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]]
matrix

[[row[i] for row in matrix] for i in range(4)]

transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])
transposed

list(zip(*matrix))


# 5.3 tuples and sequences
'''
A tuple consists of a number of values separated by commas, for instance:'''
t = 12345, 54321, 'hello!'
'''
The statement t = 12345, 54321, 'hello!' is an example of tuple packing: 
the values 12345, 54321 and 'hello!' are packed together in a tuple. 
The reverse operation is also possible:
    x, y, z = t
This is called, appropriately enough, sequence unpacking and works for any sequence 
on the right-hand side. Sequence unpacking requires that there are as many variables 
on the left side of the equals sign as there are elements in the sequence.
'''

t[0]
u = t, (1,2,3)
u
# tuples are immutable
t[0] = 888

'''
Though tuples may seem similar to lists, they are often used in different situations and for different purposes. 
Tuples are immutable, and usually contain a heterogeneous sequence of elements 
that are accessed via unpacking or indexing (or even by attribute in the case of namedtuples). 
Lists are mutable, and their elements are usually homogeneous and are accessed by iterating over the list.'''

'''
Empty tuples are constructed by an empty pair of parentheses; 
a tuple with one item is constructed by following a value with a comma 
(it is not sufficient to enclose a single value in parentheses).'''
empty = ()
singleton = 'hello',   # note trailling comma
len(empty)
len(singleton)
singleton


# 5.4 Sets
'''
A set is an unordered collection with no duplicate elements. 
Basic uses include membership testing and eliminating duplicate entries. 
Set objects also support mathematical operations like union, intersection, 
difference, and symmetric difference.

Curly braces or the set() function can be used to create sets. 
Note: to create an empty set you have to use set(), not {}; 
the latter creates an empty dictionary'''
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
basket

a = set('abracadebra')
b = set('alacazem')
a
b
a - b
a | b
a & b
a ^ b   ## letters in a or b but not both

'''
Similarly to list comprehensions, set comprehensions are also supported:'''
a = {x for x in 'abracdadabra' if x not in 'abc'}
a


# 5.5 Dictionaries
'''
The dict() constructor builds dictionaries directly from sequences of key-value pairs:'''
dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
dict([['sape', 4139], ['guido', 412], ['jack', 4098]])

'''
In addition, dict comprehensions can be used to create dictionaries from arbitrary key and value expressions:'''
{x: x**2 for x in (2, 4, 6)}

'''
When the keys are simple strings, it is sometimes easier to specify pairs using keyword arguments:'''
dict(sape=4139, guido=4127, jack=4098)


# 5.6 Looping Techniques
'''
When looping through a sequence, the position index and corresponding value can
be retrieved at the same time using the enumerate() function.'''
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

'''
To loop over two or more sequences at the same time, the entries can be paired
with the zip() function.'''
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}? It is {1}'.format(q, a))

'''
To loop over a sequence in reverse, first spicify the sequence in a forward direction
and then can reversed() function.'''
for i in reversed(range(1, 10, 2)):
    print(i)

'''
To loop over a sequence in sorted order, use the sorted() function which returns
a new sorted list while leaving the source unaltered.'''
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)

'''
It is sometimes tempting to change a list while you are looping over it, however,
it is often simpler and safer to create a new list instead:'''
import math
raw_data = [56.2, float('nan'), 51.7, 55.3, 52.5, float('nan'), 47.5]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)
filtered_data
[value for value in raw_data if not math.isnan(value)]



# 6.Modules
'''
If you quit from Python interpreter and enter it again, the definitions you have
made (functions and variables) are lost. Therefore, if you want to write a
somewhat longer program, you are better off using a text editor to prepare the 
input for the interpreter and running it with that file as input instead. This
is known as creating a script. As your program gets longers, you may want to 
split it into several files for easier maintenance. You may also want to use a 
handy function that you've written in several programs withouth copying its definition
into each program.

To support this Python has a way to put definitions in a file and use them in 
script or in an interactive instance of the interpreter. Such a file is called
a module; definitions from a module can be imported into other modules or into the main
module (the collection of variables that you have access to in a script 
exected at the top level and in calculator mode).

A module is a file containing Python definitions and statements. The file name is the 
module name with suffix .py appended. Within a module, the module's name (as a string)
is available as the value of the global variable __name__. 
'''
import pandas as pd
pd.__name__

'''
The variable sys.path is a list of strings that determines the interpreter’s 
search path for modules. 
You can modify it using standard list operations:'''
import sys
sys.path
sys.path.append('C:\\Users\\z.chen7\\Downloads\\Python')
import fibo
fibo.__name__

fibo.fib(1000)
fibo.fib2(100)

# 6.1.1 Executing modules as scripts
'''
When you run a Python module with

python fibo.py <arguments>

the code in the module will be exected, just as if you imported it, but with
the __name__ set to "__main__". 
That means that by adding this code at the end of your module:
    
if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))
    
you can make the file usable as a script as well as an importable module, 
because the code that parses the command line only runns if the module is executed
as the "main" file:
    
$ python file.py 50

if the module is imported, the code is not run:
    
import fibo

This is often used either to provide a convenient user interface to a module,
or for testing purposes (running the module as a script executes a test suite).'''


# 6.3 The dir() Function
'''
The built-in function dir() is used to find out which name a module defines.
It return a sorted list of strings:'''
import fibo, sys
dir(fibo)
dir(sys)

'''
dir() does not list the names of built-in functions and variables. If you want 
a list of those, they are defined in the standard module builtins:'''
import builtins
dir(builtins)


# 6.4 Packages
'''
Packages are a way of structuring Python's module namespace by using 'dotted module
names'. 

The __init__.py files are required to make Python treat directories containing 
the file as packages. 

Note that when using from package import item, the item can be either a 
submodule (or subpackage) of the package, or some other name defined in 
the package, like a function, class or variable.'''


# 7.1. Fancier Output Formatting
'''
The str() function is meant to return representations of values which are fairly
human-readable while repr() is meant to generate representations which can be 
read by the interpreter.
'''
s = 'Hello, world.'
str(s)
repr(s)
str(1/7)
repr(1/7)

# 7.1.1 Formatted String Literals
import math
print(f'The value of pi is approximately {math.pi:.3f}.')

'''
Passing an integer after the ':' will cause that field to be a minimum number of characters wide. This is useful for making columns line up.'''
table = {'sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print(f'{name:10}==> {phone:10}')


table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; Decab: {0[Dcab]:d}'.format(table))
print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab:{Dcab:d}'.format(**table))

for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))


# 7.2 Reading and Writing Files
'''
open() returns a file object, and is most commonly used with two arguments:
    open(filename, mode)

mode can be 'r' when the file will only be read, 
'w' for only writing (an existing file with the same name will be erased), 
and 'a' opens the file for appending; any data written to the file is automatically added to the end. 
'r+' opens the file for both reading and writing. 
The mode argument is optional; 'r' will be assumed if it’s omitted.

It is good practice to use the with keyword when dealing with file objects. 
The advantage is that the file is properly closed after its suite finishes, 
even if an exception is raised at some point.
'''
with open('workfile') as f:
    read_data = f.read()
f.close()   #True



# 7.2.2 Saving structured data with json
'''
The standard module called json can take Python data hierarchies, and convert 
them to string representations; this process is called serializing. 
Reconstructing the data from the string representation is called deserializing. 
Between serializing and deserializing, the string representing the object 
may have been stored in a file or data, or sent over a network connection to 
some distant machine.'''
import json
x = json.dumps([1, 'simple', 'list'])
x
json.loads(x)


# 8.3 Handling Exceptions
while True:
    try:
        x = int(input('Please enter a number: '))
        break
    except ValueError:
        print("Oops!, That was no valid number. Try again...")
'''
The try statement works as follows.
1. First, the try clause (the statement(s) between the try and except keywords) is executed.
2. If no exception occurs, the except clause is skipped and execution of the try statement is finished.
3. If an exception occurs during execution of the try clause, the rest of the clause is skipped. 
Then if its type matches the exception named after the except keyword, the except clause is executed, and then execution continues after the try statement.
4. If an exception occurs which does not match the exception named in the except clause, it is passed on to outer try statements; if no handler is found, 
it is an unhandled exception and execution stops with a message as shown above.
'''
'''
The try … except statement has an optional else clause, which, when present, 
must follow all except clauses. It is useful for code that must be executed 
if the try clause does not raise an exception. 
The use of the else clause is better than adding additional code to the try 
clause because it avoids accidentally catching an exception that wasn’t raised 
by the code being protected by the try … except statement.
'''
import sys
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except OSError:
        print('Cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()
'''
The except clause may specify a variable after the exception name. 
The variable is bound to an exception instance with the arguments stored in instance.args. 
For convenience, the exception instance defines __str__() so the arguments can be printed directly without having to reference .args. 
'''
try:
    raise Exception('spam', 'eggs')
except Exception as inst:
    print(type(inst))
    print(inst.args)
    print(inst)
    
    x, y = inst.args
    print('x =', x)
    print('y =', y)


# 8.4 Raising Exceptions
raise NameError('HiThere')

'''
The sole argument to raise indicates the exception to be raised. 
This must be either an exception instance or an exception class (a class that derives from Exception). 
If an exception class is passed, it will be implicitly instantiated by calling its constructor with no arguments:
'''
raise ValueError  # shorthand for 'raise ValueError()'

'''
If you need to determine whether an exception was raised byt don't intend to handle it, a simpler form of the raise
statement allows you to re-raise the exception:'''
try:
    raise NameError('HiThere')
except NameError:
    print('An exception flew by!')
    raise


# 8.5 User-defined Exceptions
''' 
When creating a module that can raise several distinct errors, 
a common practice is to create a base class for exceptions defined by that module, 
and subclass that to create specific exception classes for different error 
conditions:''' 
class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class InputError(Error):
    """Exception raised for errors in the input.
    
    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

class TransitionError(Error):
    """Raised when an operation attempts a state transition that's not allowed.
    
    Attributes:
        previous -- state at beginning of transition
        next -- attempted new state
        message -- explanation of why the specific transition is not allowed
    """
    
    def __init__(self, previous, next, message):
        self.previous = previous
        self.next = next
        self.message = message

# 8.6 Defining clean-up actions
'''
The try statement has another optional clause which is intended to define 
clean-up actions that must be executed under all circumstances. 

A finally clause is always executed before leaving the try statement, 
whether an exception has occurred or not. 
When an exception has occurred in the try clause and has not been handled by 
an except clause (or it has occurred in an except or else clause), 
it is re-raised after the finally clause has been executed.

In real world applications, the finally clause is useful for releasing 
external resources (such as files or network connections), 
regardless of whether the use of the resource was successful.
'''
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zeor!")
    except:
        print("result is", result)
    finally:
        print("executing finally clause")
divide(2, 1)
divide(2, 0)
divide('2', '1')


# 8.7 Predefined clean-up actions
"""
The with statement allows objects like files to be used in a way 
that ensures they are always cleaned up promptly and correctly.

After the statement is executed, the file f is always closed, 
even if a problem was encountered while processing the lines. 
"""
with open("myfile.txt") as f:
    for line in f:
        print(line, end="")























