>>> for line in open("myfile.txt"):
... print(line, end="")
  File "<stdin>", line 2
    print(line, end="")
    ^
IndentationError: expected an indented block after 'for' statement on line 1
>>> for line in open("myfile.txt"):
...     print(line, end="")
... 
12345667>>> with open("myfile.txt") as f:
...     for line in f:
...             print(line, end="")
... 
12345667>>> 
