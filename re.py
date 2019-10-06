# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 13:35:55 2019

@author: z.chen7
"""
# Python Regex: re.match(), re.search(), re.findall() with Example
import re
'''
\d = any number (a digit)
\s = space (tab, space, newline etc.)
\w = letters(including '_')

+ = 1 or more
? = 1 or 0
* = 0 or more
$ = the end of a string 
^ = the start of a string
'''

# Example of w+ and ^ Expression
xx =  "guru99, education is fun"
r1 = re.findall(r"^\w+", xx)
r2 = re.findall(r'\w+', xx)
r3 = re.findall(r'^\w', xx)
r4 = re.findall(r'\w', xx)

print(r1)
print(r2)
print(r3)
print(r4)

# Example of \s expression in re.split function
xx = 'we are splitting the words'
re.split(r'\s', xx)
re.split(r'\S', xx)
re.split(r's', xx)


# Using re.match().groups()
# The match method checks for a match only at the beginning of the string 
list_list = ["guru99 get", "guru99 give", "guru Selenium"]

for element in list_list:
    z = re.match(r'(g\w+)\s(g\w+)', element)
    if z:
        print(z.groups())


# Finding Pattern in Text (re.search())
# re.search checks for a match anywhere in the string.
patterns = ['software testing', 'guru99']
text = 'software testing if fun?'

for pattern in patterns:
    print('Looking for "%s" in "%s" ->' % (pattern, text), end=' ')
    
    if re.search(pattern, text):
        print('found a match!')
    else:
        print('no match!')

re.search('software', text)
re.match('software', text)
"""
search ⇒ find something anywhere in the string and return a match object.

match ⇒ find something at the beginning of the string and return a match object.
"""

# Using re.findall for text
# Re.findall() module is used when you want to iterate over the lines of the file, it will return a list of all the matches in a single step. 
abc = 'guru99@google.com, careerguru-99@hotmail.com, use.rs@yahoomail.com'
re.findall(r'[\w\.-]+@[\w\.-]+', abc)
 

# Example of re.M or Multiline Flags
xx = """guru99 
Gareerguru99	
gelenium"""

re.findall(r'^g\w+', xx)
re.findall(r'^g\w+', xx, re.MULTILINE)
re.findall(r'^g\w+', xx, re.MULTILINE | re.I)


# What does the “yield” keyword do?

# iterables
"""
iterables are handy because you can read them as much as you wish, 
but you store all the values in memory and this is not always what you want when you have a lot of values.
"""

# generators
"""
Generators are iterators, a kind of iterable you can only iterate over once. 
Generators do not store all the various in memory, they generate the vlaues on the fly."""
mygenerator = (x*x for x in range(3))
mygenerator
for i in mygenerator:
    print(i)
list(mygenerator)

# yield
"""
yield is a keyword that is used like return, except the function will return a generator"""

def createGenerator():
    mylist = range(3)
    for i in mylist:
        yield i*i

mygenerator = createGenerator()   # create a generator
print(mygenerator)    # mygeneator is an object
for i in mygenerator:
    print(i)

"""
To master yield, you must understand that when you call the function, the code you have 
written in the function body does not run.
The function only returns the generator object."""







# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 16:55:34 2019

@author: z.chen7
"""

import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
    Mr. T
_

mat
cat
bat
'''

sentence = 'Start a sentence and then bring it to an end'

text_to_search

#pattern = r'[89]00[.-]\d{3}[.-]\d{4}'
#pattern = r'[^b]at'
pattern = r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*'
pattern = re.compile(pattern)
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match.group(0))

subbed_urls = pattern.sub(r'\1', text_to_search)
print(subbed_urls)

matches_all = pattern.findall(text_to_search)
print(matches_all)

text_to_search[1:4]

import sys
print(sys.executable)

with open(r'C:\Users\z.chen7\Downloads\Python\regular expression\data.txt', 'r', encoding='utf-8') as f:
    contents = f.read()
    pattern = re.compile(r'[89]00[.-]\d{3}.\d{4}')
    matches = pattern.finditer(contents)
    
    for match in matches:
        print(match)
contents


#with open(r'C:\Users\z.chen7\Downloads\Python\regular expression\data.txt', 'r') as f:
#    contents = f.read()
   
#contents

sentence = 'Start a sentence and then bring it to an end'

pattern = re.compile(r'start', re.I)
matches = pattern.search(sentence)
matches.group(0)

pattern.match(sentence).group(0)


