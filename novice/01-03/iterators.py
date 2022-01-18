# for element in [1, 2, 3]:
#     print(element)

# for element in (1, 2, 3):
#     print(element)

# for key in {'one':1, 'two':2}:
#     print(key)

# for char in "123":
#     print(char)

# for line in open("myfile.txt"):
#     print(line, end='')

# >>> s = "abc"
# >>> it = iter(s)
# >>> print (it)
# <str_iterator object at 0x7f7348dcfa90>
# >>> next (it)
# 'a'
# >>> next (it)
# 'b'
# >>> next (it)
# 'c'
# >>> next (it)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# StopIteration

from operator import index


class Reverse:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

rev = Reverse('spam')
iter(rev)

for char in rev:
    print(char)