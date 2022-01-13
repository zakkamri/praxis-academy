>>> import sys
>>> sys.ps1
'>>> '
>>> sys.ps2
'... '
>>> sys.ps1 = 'C>'
C> print('Yuck')
  File "<stdin>", line 1
    print('Yuck')
IndentationError: unexpected indent
C>print("YUCK")
YUCK
