>>> tel = {'jack': 4098, 'sape': 4139}
>>> tel['guido']=4127
>>> tel
{'jack': 4098, 'sape': 4139, 'guido': 4127}
>>> tel['jack']
4098
>>> del tel['sape']
>>> tel
{'jack': 4098, 'guido': 4127}
>>> tel['irv']=4127
>>> tel
{'jack': 4098, 'guido': 4127, 'irv': 4127}
>>> list(tel)
['jack', 'guido', 'irv']
>>> sort(tel)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'sort' is not defined. Did you mean: 'sorted'?
>>> sorted(tel)
['guido', 'irv', 'jack']
>>> 'guido' in tel
True
>>> "harun" not in tel
True
>>> "jack" not in tel
False
>>> dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
{'sape': 4139, 'guido': 4127, 'jack': 4098}
>>> {x: x**2 for x in (2, 4, 6)}
{2: 4, 4: 16, 6: 36}
>>> dict(sape=4139, guido=4127, jack=4098)
{'sape': 4139, 'guido': 4127, 'jack': 4098}
