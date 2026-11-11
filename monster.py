import random
class Monster:
    name = "Monster"
    hp_base = 20
    attack_base = 6
    gold_range = (4, 9)
    xp = 12
    drop = None
    def __init__(self):
        self.hp = self.hp_base
    def attack(self):
        return random.randint(max(1, self.attack_base - 2), self.attack_base + 2)
    def rewards(self):
        return random.randint(*self.gold_range), self.xp, self.drop

class Slime(Monster):
    name, hp_base, attack_base, xp, drop = "Slime", 18, 5, 12, "herb"
class Goblin(Monster):
    name, hp_base, attack_base, xp, drop = "Goblin", 26, 8, 16, "potion"
class Wolf(Monster):
    name, hp_base, attack_base, xp, drop = "Wolf", 32, 9, 20, "herb"
class Skeleton(Monster):
    name, hp_base, attack_base, xp, drop = "Skeleton", 40, 11, 24, "ether"
class Shadow(Monster):
    name, hp_base, attack_base, xp, drop = "Shadow", 48, 13, 28, "potion"
class Boss(Monster):
    name, hp_base, attack_base, xp, drop = "Shadow King", 100, 16, 100, "relic"
    def attack(self):
        return super().attack() + random.choice([0, 0, 5])
MONSTERS = [Slime, Goblin, Wolf, Skeleton, Shadow]
