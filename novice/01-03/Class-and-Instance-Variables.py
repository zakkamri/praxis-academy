# class Dog:
#     kind = "Canine"
#     def __init__(self, name):
#         self.name = name

# d = Dog("Fido")
# e = Dog("Buddy")

# # print (d.kind)
# # print (e.kind)

# print (d.name)
# print (e.name)

# class Dog:
#     tricks = []
#     def __init__(self, name):
#         self.name = name

#     def add_trick(self, trick):
#         self.tricks.append(trick)

# d = Dog("Fido")
# e = Dog("Buddy")
# d.add_trick("roll over")
# e.add_trick("play dead")

# print (d.tricks)


class Dog:
    def __init__(self, name):
        self.name = name
        self.tricks = []

    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog("Fido")
e = Dog("Buddy")
d.add_trick("roll over")
e.add_trick("play dead")
#print (d.tricks)

print (e.tricks)