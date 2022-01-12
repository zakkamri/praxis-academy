>>> def make_incrementor(n):
...     return lambda x: x + n
... 
>>> f = make_incrementor(42)
>>> f(0)
42
>>> f(2)
44
>>> f(3)
45
>>> pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
>>> pairs.sort(key=lambda pair: pair[1])
>>> pairs
[(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]
>>> pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
>>> pairs
[(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
>>> aku = kamu
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'kamu' is not defined
>>> aku = "kamu"
>>> aku
'kamu'
>>> def my_function():
...     """Do nothing, but document it.
...     No, really, it doesn't do anything.
...     """
...     pass
... 
>>> print(my_function.__doc__)
Do nothing, but document it.
	No, really, it doesn't do anything.
	
>>> def f(ham: str, eggs: str = 'eggs') -> str:
...     print("Annotations:", f.__annotations__)
...     print("Arguments:", ham, eggs)
...     return ham + ' and ' + eggs
... f('spam')
  File "<stdin>", line 5
    f('spam')
    ^
SyntaxError: invalid syntax
