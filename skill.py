class Skill:
    name = "Skill"
    cooldown = 0
    cost = 0
    def use(self, player, monster):
        raise NotImplementedError

class PowerStrike(Skill):
    name = "Power Strike"
    cooldown = 2
    cost = 5
    def use(self, player, monster):
        damage = player.attack + 10
        monster.hp -= damage
        return f"Power Strike deals {damage} damage!"

class Heal(Skill):
    name = "Heal"
    cooldown = 3
    cost = 7
    def use(self, player, monster):
        healed = min(25, player.max_hp - player.hp)
        player.hp += healed
        return f"You heal {healed} HP!"

class Fireball(Skill):
    name = "Fireball"
    cooldown = 3
    cost = 9
    def use(self, player, monster):
        damage = 22 + player.level * 3
        monster.hp -= damage
        return f"Fireball deals {damage} damage!"

SKILLS = {"strike": PowerStrike, "heal": Heal, "fireball": Fireball}
