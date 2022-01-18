class MyClass:
    """A Simple Example Class"""
    i = 12345

    def f(self):
        return "Hello World"

x = MyClass()
x.f()
xf = x.f
while True:
    print(xf())