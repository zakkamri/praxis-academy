>>> knights = {'gallahad': 'the pure', 'robin': 'the brave'}
>>> for k, v in knights.items():
...     print(k,v)
... 
gallahad the pure
robin the brave
>>> for i, v in enumerate(['tic', 'tac', 'toe']):
...     print(i,v)
... 
0 tic
1 tac
2 toe
>>> questions = ['name', 'quest', 'favorite color']
>>> answers = ['lancelot', 'the holy grail', 'blue']
>>> for qu, a in zip(questions, answers):
questions  quit(      
>>> for questions, answers in zip(questions, answers):
...     print('What is your{0} It is{1}.'.format(q,a))
... 
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
NameError: name 'q' is not defined
>>> questions = ['name', 'quest', 'favorite color']
>>> answers = ['lancelot', 'the holy grail', 'blue']
>>> for questions, answers in zip(questions, answers):
...     print('What is your{0} It is{1}.'.format(questions,answers))
... 
What is yourname It islancelot.
What is yourquest It isthe holy grail.
What is yourfavorite color It isblue.
>>>     print('What is your{0}? It is{1}.'.format(questions,answers))
  File "<stdin>", line 1
    print('What is your{0}? It is{1}.'.format(questions,answers))
IndentationError: unexpected indent
>>> questions = ['name', 'quest', 'favorite color']
>>> answers = ['lancelot', 'the holy grail', 'blue']
>>> for questions, answers in zip(questions, answers):
...     print('What is your{0}? It is{1}.'.format(questions,answers))
... 
What is yourname? It islancelot.
What is yourquest? It isthe holy grail.
What is yourfavorite color? It isblue.
>>> questions = ['name', 'quest', 'favorite color']
>>> answers = ['lancelot', 'the holy grail', 'blue']
>>> for q, a in zip(questions, answers):
...     print('What is ur {0}? It is {1}.'.format(q, a))
... 
What is ur name? It is lancelot.
What is ur quest? It is the holy grail.
What is ur favorite color? It is blue.
>>> for i in reversed(range(1, 10, 2)):
...     print(i)
... 
9
7
5
3
1
>>> basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
>>> for i in sorted(basket):
...     print(i)
... 
apple
apple
banana
orange
orange
pear
>>> basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
>>> for f in sorted(set(basket)):
...     print(f)
... 
apple
banana
orange
pear
>>> import math
>>> raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
>>> filtered_data = []
>>> for value in raw_data:
...     if not math.isnan(value):
...             filtered_data.append(value)
... 
>>> filtered_data
[56.2, 51.7, 55.3, 52.5, 47.8]
