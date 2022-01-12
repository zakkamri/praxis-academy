#default argument values
#from typing import Concatenate


#def ask_ok(prompt, retries=4, reminder='please try again'):
 #   while True:
  #      ok=input(prompt)
   #     if ok in('y', 'ye', 'yes'):
    #        return True
     #   if ok in('n', 'no', 'nop', 'nope'):
      #      return False
       # retries=retries - 1
        #if retries<0:
         #   raise ValueError('invalid user response')
        #print(reminder)

#ask_ok('Do you really want to quit?')
#ask_ok('OK to overwrite the file?', 2)
#ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')

#i=5
#def f(arg=i):
 #   print(arg)

#i=6
#f()

#def f(a, L=[]):
 #   L.append(a)
  #  return L
#print(f(1))
#print(f(2))
#print(f(3))

#def f(a, L=None):
 #   if L is None:
  #      L=[]
   # L.append(a)
    #return L

#keywords argument
#def parrot(voltage , state='a stiff', action='voom', type='Norwegian Blue'):
  #  print("-- This parrot wouldn't", action, end='')
   # print("if you put", voltage, "volts through it.")
    #print("--lovely plumage, the", type)
    #print("--It's", state, "!")

#parrot(1000)
#parrot(voltage=1000)
#parrot(voltage=1000000, action='VOOOOOM')
#parrot('a million', 'bereft of life', 'jump')

#def coba(satu, dua, tiga):
#    print(f"{satu}, {dua}, {tiga}")

#coba("burung", "kakak")

#def function(a):
# pass

#function(0, a=0)

#def cheeseshop(kind, *arguments, **keywords):
 #   print("-- Do you have any", kind, "?")
  #  print("-- I'm sorry, we're all out of", kind)
   # for arg in arguments:
    #    print(arg)
    #print("-" * 40)
    #for kw in keywords:
     #   print(kw, ":", keywords[kw])

#cheeseshop("Limburger", "It's very runny, sir.",
 #          "It's really very, VERY runny, sir.",
  #         shopkeeper="Michael Palin",
   #        client="John Cleese",
    #       sketch="Cheese Shop Sketch")

# special parameters
# function examples

#def standard_arg(arg):
 #    print(arg)

#def pos_only_arg(arg, /):
 #    print(arg)

#def kwd_only_arg(*, arg):
 #    print(arg)

#def combined_example(pos_only, /, standard, *, kwd_only):
 #    print(pos_only, standard, kwd_only)
#standard_arg(2)
#standard_arg(arg=2)

#pos_only_arg(arg=1)
#kwd_only_arg(3)
#kwd_only_arg(arg=3)
#combined_example(1, 2, 3)

#combined_example(1, 2, kwd_only=3)
#combined_example(1, standard=2, kwd_only=3)
#combined_example(pos_only=1, standard=2, kwd_only=3)

#def foo(name, **kwds):
#    return 'name' in kwds
#
#foo(1, **{'name': 2})

#def foo(name, /, **kwds):
#    return 'name' in kwds

#foo(1, **{'name': 2})
#True

# 4.8.3.5. Recap
#def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):

#4.8.4. Arbitary Argument Lists

def write_multiple_items(file, separator, *args):
    file.write(separator.join(args))

def concat(*args, sep="/"):
    return sep.join(args)

concat("earth", "mars", "venus")
concat("earth", "mars", "venus", sep=".")