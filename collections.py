# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 16:39:17 2019

@author: z.chen7
"""

from collections import Counter, namedtuple, OrderedDict, defaultdict, deque

# Counter
a = "aaaaaaaaaaaaaaaaabbbbbbbcc"
my_counter = Counter(a)
my_counter
my_counter.most_common(1)
my_counter.most_common(1)[0][0]
list(my_counter.elements())


# namedtuple
Point = namedtuple("Point", "x, y, z")
a = Point(3, 4, 5)
a
a.x
a.y
a.z
a._asdict()
a._fields
a._replace(x=10)


# OrderedDict
d = OrderedDict()
d['a'] = 1
d['b'] = 2
d['c'] = 3
d
d.keys()


# defaultdict
d = defaultdict(bool)
d['a'] = 1
d['b'] = 2
d['c']


# deque
d = deque([1])
d

d.append(2)
d.appendleft(0)
d

d.pop()
d.popleft()
d

d.extend([2, 3])
d.extendleft([0, -1])    # extend [-1, 0] to the left
d

d.rotate(1)
d
d.rotate(-1)
d

d_max = deque("hello", maxlen=5)
d_max.appendleft("A")
d_max
d_max.extendleft(["B", "C"])
d_max



# 8.3 collections - High-performance container datatypes

from collections import Counter
import re

# 8.3.1 Counter Objects
# A counter tool is provided to support convenient and rapid tallies.

# Tally occurences of words in a list
cnt = Counter()
for word in ['red','blue','red','green','blue','blue']:
    cnt[word] += 1    
print(cnt)

# Find the ten most common words in Hamlet
path = 'c:/users/z.chen7/Downloads/Python/hamlet.txt'
words = re.findall(r'\w+', open(path).read().lower())
Counter(words).most_common(10)

# Elements are counted from an iterable or initialized from another mapping
c = Counter()
c = Counter('gallahad')
c['gallahad']
c = Counter(['gallahad'])
c
c = Counter({'red': 4, 'blue': 2})
c
c = Counter(cats=4, dogs=8)
c
c['rabbit']
c['rabbit'] = 0
c
del c['rabbit']
c

# Counter objects support three methods beyond those available for all dictionaries
# elements()
c = Counter(a=4, b=2, c=0, d=-2)
list(c.elements())

# most_common([n])
Counter('abracadabra').most_common(3)

# subtract()
c = Counter(a=4, b=2, c=0, d=-2)
d = Counter(a=1, b=2, c=3, d=4, e=-1)
c.subtract(d)
c


# Common patterns for working with Counter object:
c.values()
sum(c.values())
c.clear() 
list(c)
set(c)
c.items()

list_of_pairs = [('a',3), ('b', 2), ('c', -1)]
dict(list_of_pairs)
Counter(dict(list_of_pairs))

c.most_common()[:-3:-1]
c.most_common()[-2:]

c += Counter()
c

# mathematical operations and intersection and union
c = Counter(a=3, b=1)
b = Counter(a=1, b=2)
c + b
c - b
c & b
c | b



# 8.3.2 deque objects
from collections import deque
d = deque('ghi')
d

for elem in d:
    print(elem.upper())

d.append('j')
d.appendleft('f')
d

d.pop()
d.popleft()
list(d)

d[0]
d[-1]
list(reversed(d))
'h' in d

d.extend('jkl')
d

d.rotate(1)   # right rotate
d
d.rotate(-1)   # left rotate
d

deque(reversed(d))
d.clear()
d
d.pop()

d.extendleft('abc')
d


