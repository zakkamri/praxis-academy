>>> buah=["jeruk", "nanas", "apel", "jeruk", "mangga", "jeruk", "nanas", "apel"]
>>> buah.count("jeruk")
3
>>> buah.count("apel")
2
>>> buah.count("nanas")
2
>>> buah.index("jeruk")
0
>>> fruits.reverse()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'fruits' is not defined
>>> buah.reverse()
>>> buah
['apel', 'nanas', 'jeruk', 'mangga', 'jeruk', 'apel', 'nanas', 'jeruk']
>>> buah.appends("anggur")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'list' object has no attribute 'appends'. Did you mean: 'append'?
>>> buah.append("anggur")
>>> buah
['apel', 'nanas', 'jeruk', 'mangga', 'jeruk', 'apel', 'nanas', 'jeruk', 'anggur']
>>> buah.sort()
>>> buah
['anggur', 'apel', 'apel', 'jeruk', 'jeruk', 'jeruk', 'mangga', 'nanas', 'nanas']
>>> buah.pop()
'nanas'
