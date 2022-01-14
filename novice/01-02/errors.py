# class B(Exception):
#     pass

# class C(B):
#     pass

# class D(C):
#     pass

# for cls in [B, C, D]:
#     try:
#         raise cls()
#     except D:
#         print("D")
#     except C:
#         print("C")
#     except B:
#         print("B")

# import sys

# try:
#     f = open('myfile.txt')
#     s = f.readline()
#     i = int(s.strip())
# except OSError as err:
#     print("OS error: {0}".format(err))
# except ValueError:
#     print("Could not convert data to an integer.")
# except BaseException as err:
#     print(f"Unexpected {err=}, {type(err)=}")
#     raise

# for arg in sys.argv[1:]:
#     try:
#         f = open(arg, 'r')
#     except OSError:
#         print('cannot open', arg)
#     else:
#         print(arg, 'has', len(f.readlines()), 'lines')
#         f.close()

>>> try:
...     raise Exception('spam', 'eggs')
... except Exception as inst:
...     print(type(inst))
...     print(inst.args)
...     print(inst)
...     x, y = inst.args
...     print('x =', x)
...     print('y =', y)
... 
<class 'Exception'>
('spam', 'eggs')
('spam', 'eggs')
x = spam
y = eggs
>>> 
>>> def this_fails():
...     x = 1/0
... 
>>> try:
...     this_fails()
... except ZeroDivisionError as err:
...     print('Handling run-time error:', err)
... 
Handling run-time error: division by zero
