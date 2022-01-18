class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health

class Hero_intelligent(Hero):
    pass

class Hero_strength(Hero):
    pass

invoker = Hero('invoker', 100)
zeus = Hero("zeus", 200)
axe = Hero("axe", 500)

print(invoker.name)
print(zeus.name)
print(axe.name)
