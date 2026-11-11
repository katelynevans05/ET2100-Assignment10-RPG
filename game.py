import random
from colorama import Fore, Style
from map import draw, move, nearby_npc
from monster import MONSTERS, Boss
from combat import battle
from inventory import show, use
from npc import talk
from quest import show as show_quests
from skill import SKILLS
from database import save_user

class Colors:
    GREEN, RED, YELLOW, BLUE, RESET = Fore.GREEN, Fore.RED, Fore.YELLOW, Fore.BLUE, Style.RESET_ALL

def help_text():
    print("W/A/S/D move | map | talk | explore | boss | travel | status | inventory | use | skills | learn | quests | rest | help | save | quit")

def play(username, player):
    print("\nLong ago, the Shadow King stole the kingdom's light...")
    print("You are its last hope. Speak with the Elder and begin your adventure!")
    help_text()
    while True:
        try:
            cmd = input("\nCommand > ").strip().lower()
            if cmd in ("w", "a", "s", "d"):
                if move(player, cmd) and player.map_name == "forest" and random.random() < 0.14:
                    battle(player, random.choice(MONSTERS)(), Colors)
            elif cmd == "map":
                draw(player, Colors)
            elif cmd == "talk":
                npc = nearby_npc(player)
                if npc:
                    talk(player, npc)
                else:
                    print("No NPC nearby. Walk next to an N on the map.")
            elif cmd == "explore":
                if player.map_name != "forest":
                    print("Travel to the forest to find monsters.")
                else:
                    battle(player, random.choice(MONSTERS)(), Colors)
            elif cmd == "boss":
                if player.map_name != "forest" or player.quests["main"] != 3 or "crystal" not in player.inventory:
                    print("The boss is locked. Complete the main quest steps first.")
                else:
                    battle(player, Boss(), Colors, boss=True)
            elif cmd == "travel":
                if player.map_name == "village":
                    player.map_name, player.x, player.y = "forest", 1, 1
                else:
                    player.map_name, player.x, player.y = "village", 1, 1
                print("Traveled to", player.map_name)
                draw(player, Colors)
            elif cmd == "status":
                player.status()
            elif cmd == "inventory":
                show(player)
            elif cmd == "use":
                use(player, input("Item key: ").strip().lower())
            elif cmd == "skills":
                for key in player.skills:
                    s = SKILLS[key]()
                    print(f"{key}: energy {s.cost}, cooldown {s.cooldown}")
            elif cmd == "learn":
                print("Learn Heal at level 2, Fireball at level 3 (free).")
                key = input("Learn skill (heal/fireball): ").strip().lower()
                required = {"heal": 2, "fireball": 3}
                if key not in required:
                    print("Unknown skill.")
                elif player.level < required[key]:
                    print("Your level is too low.")
                elif key in player.skills:
                    print("Already learned.")
                else:
                    player.skills.append(key)
                    print("Learned", key)
            elif cmd == "quests":
                show_quests(player)
            elif cmd == "rest":
                if player.map_name != "village":
                    print("You can only rest in the village.")
                else:
                    player.hp, player.energy = player.max_hp, player.max_energy
                    print("Rested. HP and energy restored.")
            elif cmd == "help":
                help_text()
            elif cmd == "save":
                save_user(username, player)
                print("Progress saved!")
            elif cmd == "quit":
                save_user(username, player)
                print("Progress saved. Goodbye!")
                return
            else:
                print("Unknown command. Type help.")
            save_user(username, player)
            if player.won:
                print("You completed the game! You can keep exploring or type quit.")
        except (KeyboardInterrupt, EOFError):
            save_user(username, player)
            print("\nProgress saved. Goodbye!")
            return
