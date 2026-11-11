from item import ITEMS
class Player:
    def __init__(self, name, data=None):
        data = data or {}
        self.name = name
        self.level = data.get("level", 1)
        self.xp = data.get("xp", 0)
        self.gold = data.get("gold", 20)
        self.max_hp = 65 + (self.level - 1) * 12
        self.hp = data.get("hp", self.max_hp)
        self.max_energy = 30 + (self.level - 1) * 4
        self.energy = data.get("energy", self.max_energy)
        self.inventory = data.get("inventory", {"potion": 2})
        self.skills = data.get("skills", ["strike"])
        self.map_name = data.get("map_name", "village")
        self.x = data.get("x", 1)
        self.y = data.get("y", 1)
        self.quests = data.get("quests", {"main": 0, "herbs": 0, "hunter": 0})
        self.kills = data.get("kills", {})
        self.won = data.get("won", False)
    @property
    def attack(self):
        return 8 + self.level * 2 + (ITEMS["sword"]["attack"] if "sword" in self.inventory else 0)
    @property
    def defense(self):
        return 2 + self.level + (ITEMS["armor"]["defense"] if "armor" in self.inventory else 0)
    def gain_xp(self, amount):
        self.xp += amount
        while self.xp >= self.level * 30:
            self.xp -= self.level * 30
            self.level += 1
            self.max_hp += 12
            self.max_energy += 4
            self.hp = self.max_hp
            self.energy = self.max_energy
            print(f"LEVEL UP! You are now level {self.level}!")
    def status(self):
        print(f"{self.name} | Level {self.level} | XP {self.xp}/{self.level * 30}")
        print(f"HP {self.hp}/{self.max_hp} | Energy {self.energy}/{self.max_energy} | Gold {self.gold}")
        print(f"Attack {self.attack} | Defense {self.defense} | Skills: {', '.join(self.skills)}")
    def to_dict(self):
        return {key: getattr(self, key) for key in ("level", "xp", "gold", "hp", "energy", "inventory", "skills", "map_name", "x", "y", "quests", "kills", "won")}
