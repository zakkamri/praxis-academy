stack=[3,4,5]
>>> stack.append
<built-in method append of list object at 0x7fda9d09fd00>
>>> stack.append(6)
>>> stack
[3, 4, 5, 6]
>>> stack.append(6,7)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: list.append() takes exactly one argument (2 given)
>>> stack.append(7)
>>> stack
[3, 4, 5, 6, 7]
>>> stack.pop
<built-in method pop of list object at 0x7fda9d09fd00>
>>> stack.pop()
7
>>> stack.pop()
6
>>> stack
[3, 4, 5]
>>> stack.pop()
5
>>> stack
[3, 4]
