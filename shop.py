from item import ITEMS
from inventory import add

def visit(player):
    keys = ["potion", "ether", "sword", "armor"]
    while True:
        print(f"SHOP - Your gold: {player.gold}")
        for i, key in enumerate(keys, 1):
            print(f"{i}. {ITEMS[key]['name']} - {ITEMS[key]['price']} gold")
        choice = input("Buy number or B to go back: ").strip().lower()
        if choice == "b":
            return
        if not choice.isdigit() or not 1 <= int(choice) <= len(keys):
            print("Invalid choice.")
            continue
        key = keys[int(choice)-1]
        if key in ("sword", "armor") and key in player.inventory:
            print("You already own this equipment.")
        elif player.gold < ITEMS[key]["price"]:
            print("Not enough gold.")
        else:
            player.gold -= ITEMS[key]["price"]
            add(player, key)
            print("Purchased!")
