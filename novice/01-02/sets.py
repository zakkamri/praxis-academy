>>> basket = ('apple', 'orange', 'apple', 'pear', 'orange', 'banana')
>>> set(basket)
{'apple', 'banana', 'orange', 'pear'}
>>> a = set('abracadabra')
>>> b = set('alacazam')
>>> a
{'b', 'c', 'd', 'a', 'r'}
>>> v
([1, 2, 3], [3, 2, 1])
>>> b
{'l', 'm', 'c', 'z', 'a'}
>>> a - b
{'d', 'b', 'r'}
>>> a | b
{'z', 'l', 'b', 'm', 'c', 'd', 'a', 'r'}
>>> a & b 
{'a', 'c'}
>>> a ^ b 
{'d', 'b', 'm', 'z', 'l', 'r'}
>>> a = {x for x in 'abracadabra' if x not in 'abc'}
>>> a
{'d', 'r'}
>>> a = {x for x in 'abracadabra' if x not in 'bra'}
>>> a
{'d', 'c'}
>>> a = {a for a in 'abracadabra' if a not in 'bra'}
>>> a
{'d', 'c'}
