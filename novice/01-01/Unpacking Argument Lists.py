>>> list(range(3, 6))
[3, 4, 5]
>>> args = [3, 6]
>>> list(range(*args)) 
[3, 4, 5]
>>> def parrot(voltage, state='a stiff', action='voom'):
...     printprint("-- This parrot wouldn't", action, end=' ')
... 
>>> 
>>> 
>>> def parrot(voltage, state='a stiff', action='voom'):
...     print("-- This parrot wouldn't", action, end=' ')
...     print("if you put", voltage, "volts through it.", end=' ')
...     print("E's", state, "!")
... 
>>> d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
>>> parrot(**d)
-- This parrot wouldn't VOOM if you put four million volts through it. E's bleedin' demised !
