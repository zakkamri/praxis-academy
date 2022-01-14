>>> raise RuntimeError from exc
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'exc' is not defined. Did you mean: 'exec'?
>>> def func():
...     raise
... 
>>> try:
...     func()
... except ConnectionError as exc:
...     raise RunTimeError('Failed to open database') from exc
... 
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
  File "<stdin>", line 2, in func
RuntimeError: No active exception to reraise

>>> try:
...     open('database.sqlite')
... except OSError:
...     raise RuntimeError from None
... 
Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
RuntimeError
