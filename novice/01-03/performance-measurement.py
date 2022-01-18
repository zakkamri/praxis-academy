>>> from timeit import Timer
>>> Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()
0.020252463999895554
>>> Timer('a,b = b,a', 'a=1; b=2').timeit()
0.02722461099983775
