>>> list.append(x)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'x' is not defined
>>> x = 123456
>>> list.append(x)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: descriptor 'append' for 'list' objects doesn't apply to a 'int' object
>>> x = 20092
>>> list.append(x)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: descriptor 'append' for 'list' objects doesn't apply to a 'int' object
>>> x = aku
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'aku' is not defined
>>> x = "aku"
>>> list.append(x)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: descriptor 'append' for 'list' objects doesn't apply to a 'str' object
>>> fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
>>> fruits.count('apple')
2
>>> buah = ["jambu", "kedondong", "jambu", "jeruk", "nanas", "jeruk"]
>>> buah.count('jambu')
2
>>> fruits.reverse()
>>> fruits
['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']
>>> fruits.sort()
>>> fruits
['apple', 'apple', 'banana', 'banana', 'kiwi', 'orange', 'pear']
>>> fruits.pop()
'pear'
>>> stack = [3, 4, 5]
>>> stack.append(6)
>>> stack.append(7)
>>> stack
[3, 4, 5, 6, 7]
>>> stack.pop()
7
>>> stack.pop()
6
>>> stack.pop()
5
>>> stack.pop()
4
>>> stack.pop()
3
>>> stack.pop()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: pop from empty list
>>> from collections import deque
>>> queue = deque(["Eric", "John", "Michael"])
>>> queue.append("Terry") 
>>> queue.append("Graham")
>>> queue.popleft()
'Eric'
>>> queue.popleft()
'John'
>>> queue
deque(['Michael', 'Terry', 'Graham'])
>>> queue.popmid()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'collections.deque' object has no attribute 'popmid'
>>> queue.popright()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'collections.deque' object has no attribute 'popright'
>>> queue = deque(["Eric", "John", "Michael"])
>>> queue.append("Terry") 
>>> queue.append("Graham")
>>> queue.popright()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'collections.deque' object has no attribute 'popright'
>>> squares=[]
>>> for x in range(10):
...     squares.append(x**2)
... 
>>> squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> squares=list(map(lambda x: x**2, range(10))
... 
... 
... 
... 
... 
... 
... 
... 
... 
... 
... 
... 
... 
... pass
  File "<stdin>", line 15
    pass
    ^^^^
SyntaxError: invalid syntax
>>> squares=list(map(lambda x: x**2, range(10)))
>>> squares=[x**2 for x in range(10)]
>>> [(x,y) for x in [1,2,3] for y in [3,1,4] if x !=y]
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
>>> comb[]
  File "<stdin>", line 1
    comb[]
         ^
SyntaxError: invalid syntax
>>> combs=[]
>>> for x in [1,2,3]:
...     for y in[3,1,4]:
...             if x !=y:
...                     combs.append((x,y))
... 
>>> combs
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]