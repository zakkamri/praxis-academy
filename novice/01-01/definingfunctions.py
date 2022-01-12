def fib(n):
    """Print a Fibonacci series up to n."""
    a, b=0,1
    while a<n:
        print(a, end='')
        a,b=b, a+b
    print()

fib(2000)

fib
f = fib
f(500)

fib(0)
print(fib(0))

def fib2(n):
    result=[]
    a,b=0,1
    while a < n:
        result.append(a)
        a,b=b, a+b
    return result

f100=fib2(100)
print(f100)