# this is from https://docs.python.org/3/tutorial/interpreter.html
the_world_is_flat = True
if the_world_is_flat:
    print("Be careful not to fall off!")


# this is from https://docs.python.org/3/tutorial/controlflow.html
# if Statements
x = int(input("Please enter an integer: "))
if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')


# for Statements
# simple for statements
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))

# loop over a copy of the collection or to create a new collection
# create a sample collection
users = {'Hans' : 'active', 'Eleonore' : 'inactive', 'chineese' : 'active'}

# strategy: itterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

#strategy: create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status

# calling the users
print(users)


# for statements
for i in range(5):
    print(i)

# combine range() and len()
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])