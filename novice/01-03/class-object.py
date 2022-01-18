# def scope_test():
#     def do_local():
#         spam = "local spam"

#     def do_nonlocal():
#         nonlocal spam
#         spam = "nonlocal spam"

#     def do_global():
#         global spam
#         spam = "global spam"

#     spam = "test spam"
#     do_local()
#     print("After local assignment:", spam)
#     do_nonlocal()
#     print("After nonlocal assignment:", spam)
#     do_global()
#     print("After global assignment:", spam)

# scope_test()
# print("In global scope:", spam)
    
>>> class MyClass:
...     i = 12345
... 
>>> def f(self):
...     return 'hello world'
... 
>>> x = MyClass()
>>> def __init__(self):
...     self.data = []
... 
>>> x = MyClass()
>>> 
>>> class Complex:
...     def __init__(self, realpart, imagpart):
...             self.r = realpart
...             self.i = imagpart
... 
>>> x = Complex(3.0, -4.5)
>>> x.i, x.r
(-4.5, 3.0)