>>> f = open('workfile', 'w')
>>> with open('workfile') as f:
...     read_data = f.read()
... 
>>> f.closed
True
>>> f.read
<built-in method read of _io.TextIOWrapper object at 0x7f5860cfb9f0>
>>> f.closed()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'bool' object is not callable
