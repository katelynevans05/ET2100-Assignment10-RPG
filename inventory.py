from item import ITEMS

def add(player, key, amount=1):
    player.inventory[key] = player.inventory.get(key, 0) + amount

def remove(player, key, amount=1):
    if player.inventory.get(key, 0) < amount:
        return False
    player.inventory[key] -= amount
    if player.inventory[key] == 0:
        del player.inventory[key]
    return True

def show(player):
    if not player.inventory:
        print("Inventory is empty.")
    for key, count in player.inventory.items():
        print(f"{ITEMS[key]['name']}: {count}")

def use(player, key):
    if player.inventory.get(key, 0) < 1:
        print("You do not have that item.")
        return False
    if key == "potion":
        if player.hp == player.max_hp:
            print("HP is already full.")
            return False
        player.hp = min(player.max_hp, player.hp + ITEMS[key]['heal'])
    elif key == "ether":
        if player.energy == player.max_energy:
            print("Energy is already full.")
            return False
        player.energy = min(player.max_energy, player.energy + ITEMS[key]['energy'])
    elif key in ("sword", "armor"):
        print("Equipment works automatically while in your inventory.")
        return False
    else:
        print("This is a quest item and cannot be used.")
        return False
    remove(player, key)
    print(f"Used {ITEMS[key]['name']}!")
    return True
