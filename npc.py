import quest
from shop import visit

def talk(player, npc):
    if npc == "elder":
        quest.elder(player)
    elif npc == "merchant":
        print("Merchant: Welcome! My supplies are the finest in town.")
        visit(player)
    elif npc == "healer":
        quest.healer(player)
    elif npc == "ranger":
        quest.ranger(player)
    elif npc == "sage":
        quest.sage(player)
