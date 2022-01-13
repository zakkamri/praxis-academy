>>> f = open('workfile', 'r')
>>> f.read()
''
>>> f = open('workfile', 'w')
>>> f.write(hahaha)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'hahaha' is not defined
>>> f.write("hahaha")
6
>>> f.write("jangan begitu dong")
18
>>> f.close()
>>> f.write("jangan begitu dong")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: I/O operation on closed file.
>>> f = open('workfile', 'r')
>>> f.read()
'hahahajangan begitu dong'
>>> f.write("baru nich")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
io.UnsupportedOperation: not writable
>>> f = open('workfile', 'w')
>>> f.write("ada yg baru nich")
16
>>> f.read()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
io.UnsupportedOperation: not readable
>>> f = open('workfile', 'r')
>>> f.read()
'ada yg baru nich'
