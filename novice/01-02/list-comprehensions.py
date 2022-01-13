>>> squares = []
>>> for x in range(10):
...     squares.append(x**2)
... 
>>> squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> 
>>> list(map(lambda x: x**2, range(10)))
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> squares = [x**2 for x in range(10)]
>>> 
>>> squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> isi = [x**2 for x in range(10)]
>>> isi
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
>>> combs = []
>>> for x in [1,2,3]:
...     for y in [3,1,4]:
...             if x != y:
...                     combs.append((x, y))
... combs
  File "<stdin>", line 5
    combs
    ^^^^^
SyntaxError: invalid syntax
>>> 
>>> combs = []
>>> for x in [1,2,3]:
...     for y in [3,1,4]:
...             if x != y:
...                     combs.append((x, y))
... 
>>> combs
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

>>> vec = [-4, -2, 0, 2, 4]
>>> [x*2 for x in vec]
[-8, -4, 0, 4, 8]
>>> [x for x in vec if x >= 0]
[0, 2, 4]
>>> [abs(x) for x in vec]
[4, 2, 0, 2, 4]
>>> freshfruit = ['  banana', '  loganberry ', 'passion frui ']
>>> [weapon.strip() for weapon in freshfruit]
['banana', 'loganberry', 'passion frui']
>>> freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
>>> [weapon.strip() for weapon in freshfruit]
['banana', 'loganberry', 'passion fruit']
>>> [(x, x**2) for x in range(6)]
[(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
>>> [x, x**2 for x in range(6)]
  File "<stdin>", line 1
    [x, x**2 for x in range(6)]
     ^^^^^^^
SyntaxError: did you forget parentheses around the comprehension target?
>>> vec = [[1,2,3], [4,5,6], [7,8,9]]
>>> [num for elem in vec for num in elem]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> 
>>> [num for elem in vec for num in elem]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> from math import pi
>>> [str(round(pi, i)) for i in range(1, 6)]
['3.1', '3.14', '3.142', '3.1416', '3.14159']