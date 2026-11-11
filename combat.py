import random
from skill import SKILLS
from inventory import add, use

def battle(player, monster, color, boss=False):
    print(color.RED + f"A {monster.name} appears!" + color.RESET)
    cooldowns = {}
    turn = 0
    while player.hp > 0 and monster.hp > 0:
        turn += 1
        print(f"{player.name}: {player.hp}/{player.max_hp} HP, {player.energy} energy | {monster.name}: {max(0, monster.hp)} HP")
        action = input("[A]ttack [S]kill [I]tem [R]un: ").strip().lower()
        if action == "a":
            damage = player.attack + random.randint(0, 4)
            monster.hp -= damage
            print(f"You deal {damage} damage.")
        elif action == "s":
            print("Skills:", ", ".join(player.skills))
            key = input("Skill name: ").strip().lower()
            if key not in player.skills or key not in SKILLS:
                print("You have not learned that skill.")
                continue
            skill = SKILLS[key]()
            if cooldowns.get(key, 0) > turn:
                print(f"On cooldown for {cooldowns[key] - turn} more turn(s).")
                continue
            if player.energy < skill.cost:
                print("Not enough energy.")
                continue
            player.energy -= skill.cost
            print(skill.use(player, monster))
            cooldowns[key] = turn + skill.cooldown + 1
        elif action == "i":
            key = input("Use potion or ether: ").strip().lower()
            if not use(player, key):
                continue
        elif action == "r":
            if boss:
                print("You cannot run from the final boss!")
                continue
            if random.random() < 0.65:
                print("You escaped!")
                return "escaped"
            print("Escape failed!")
        else:
            print("Invalid action.")
            continue
        if monster.hp <= 0:
            break
        damage = max(1, monster.attack() - player.defense)
        player.hp -= damage
        print(f"{monster.name} hits you for {damage} damage.")
    if player.hp <= 0:
        print("You were defeated. You wake up in the village with restored health.")
        player.hp = player.max_hp
        player.energy = player.max_energy
        player.map_name, player.x, player.y = "village", 1, 1
        player.gold = max(0, player.gold - 5)
        return "lost"
    gold, xp, drop = monster.rewards()
    player.gold += gold
    print(color.GREEN + f"Victory! +{gold} gold, +{xp} XP" + color.RESET)
    player.kills[monster.name] = player.kills.get(monster.name, 0) + 1
    if drop and random.random() < (1.0 if boss else 0.6):
        add(player, drop)
        print(f"Found: {drop}!")
    player.gain_xp(xp)
    if boss:
        player.quests["main"] = 4
        player.won = True
        print(color.GREEN + "YOU WIN! The Lost Kingdom is saved!" + color.RESET)
    return "won"
