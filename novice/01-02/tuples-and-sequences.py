>>> t = 12345, 54321, 'hello!'
>>> t
(12345, 54321, 'hello!')
>>> t[1]
54321
>>> t[0
... 
... 
... pass
  File "<stdin>", line 4
    pass
    ^^^^
SyntaxError: invalid syntax
>>> t[0]
12345
>>> t[2]
'hello!'
>>>     u = t, (1, 2, 3, 4, 5)
  File "<stdin>", line 1
    u = t, (1, 2, 3, 4, 5)
IndentationError: unexpected indent
>>> u = t, (1, 2, 3, 4, 5)
>>> u
((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))
>>> t[0]
12345
>>> t[0] = 8888
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> v = ([1, 2, 3], [3, 2, 1])
>>> v
([1, 2, 3], [3, 2, 1])
>>> transposed [v]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: list indices must be integers or slices, not tuple
>>> transposed = [v]
>>> transposed
[([1, 2, 3], [3, 2, 1])]
>>> v
([1, 2, 3], [3, 2, 1])
>>> empty = ()
>>> singleton = 'hello'
>>> len(empty)
0
>>> len(singleton)
5
>>> empty = ()]
  File "<stdin>", line 1
    empty = ()]
              ^
SyntaxError: unmatched ']'
>>> empty = ()
>>> singleton = 'hello',
>>> len(empty)
0
>>> len(singleton)
1
>>> singleton
('hello',)
>>> x, y, z = t
>>> t
(12345, 54321, 'hello!')
