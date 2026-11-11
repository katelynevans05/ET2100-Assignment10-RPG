from inventory import add, remove

def main_description(player):
    stage = player.quests["main"]
    return ["Speak to the Village Elder (N at 3,4).",
            "Defeat 2 Goblins in the forest, then return to Elder.",
            "Find the Sage in the forest (N at 6,6).",
            "Defeat the Shadow King in the forest (use 'boss').",
            "Main quest completed!"][min(stage,4)]

def show(player):
    print("MAIN:", main_description(player))
    print("SIDE - Herbal Help:", {0:"Talk to Healer",1:"Collect 3 herbs and return to Healer",2:"Completed"}[player.quests["herbs"]])
    print("SIDE - Wolf Hunt:", {0:"Talk to Ranger",1:"Defeat 2 Wolves and return to Ranger",2:"Completed"}[player.quests["hunter"]])

def elder(player):
    if player.quests["main"] == 0:
        print("Elder: Darkness spreads. Please defeat two goblins in the forest!")
        player.quests["main"] = 1
    elif player.quests["main"] == 1 and player.kills.get("Goblin",0) >= 2:
        print("Elder: Great work! Find the Sage in the forest.")
        player.quests["main"] = 2
        player.gold += 25
    else:
        print("Elder: Our village is counting on you.")

def sage(player):
    if player.quests["main"] == 2:
        print("Sage: Take this Sun Crystal. It can break the King's shield!")
        add(player, "crystal")
        player.quests["main"] = 3
    else:
        print("Sage: Wisdom comes to those who explore.")

def healer(player):
    if player.quests["herbs"] == 0:
        print("Healer: Please bring me three herbs dropped by Slimes or Wolves.")
        player.quests["herbs"] = 1
    elif player.quests["herbs"] == 1 and player.inventory.get("herb",0) >= 3:
        remove(player, "herb", 3)
        player.quests["herbs"] = 2
        player.gold += 35
        player.gain_xp(25)
        print("Healer: Thank you! Here are 35 gold and 25 XP.")
    else:
        print("Healer: I hope you're staying healthy!")

def ranger(player):
    if player.quests["hunter"] == 0:
        print("Ranger: Defeat two Wolves to make the forest safer.")
        player.quests["hunter"] = 1
    elif player.quests["hunter"] == 1 and player.kills.get("Wolf",0) >= 2:
        player.quests["hunter"] = 2
        player.gold += 30
        player.gain_xp(30)
        print("Ranger: Nice work! Take 30 gold and 30 XP.")
    else:
        print("Ranger: Keep your eyes open in the woods.")
