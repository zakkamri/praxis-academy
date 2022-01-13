def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result


# >>> import fibo
# >>> fibo,fib(1000)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'fib' is not defined. Did you mean: 'fibo'?
# >>> fibo.fib(1000)
# 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 
# >>> fibo.fib2(100)
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# >>> fibo.__name__
# 'fibo'
# >>> fib = fibo.fib
# >>> fib(500)
# 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 
