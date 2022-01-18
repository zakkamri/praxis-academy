import re
x = re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')

a = re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')

b = "tea for too" .replace("too", "two")

print(x)
print(a)
print(b)