import random
from src.item import Item

def hunt(player, current_room):
    if not current_room.can_hunt:
        print(" Vous ne pouvez pas chasser ici.")
        return
    print(" Vous partez chasser...")
    if random.random() < 0.6:
        meat = Item("Viande", "food", heal=20)
        player.add_item(meat)
        print(" Vous avez chassé avec succès et obtenu de la viande !")
    else:
        print(" Vous etes trop nul. hahaha...")
    player.decrease_stats()

def fish(player, current_room):
    if not current_room.can_fish:
        print(" Vous ne pouvez pas pêcher ici.")
        return
    print(" Vous tentez de pêcher...")
    if random.random() < 0.5:
        fish_item = Item("Poisson", "food", heal=15)
        player.add_item(fish_item)
        print(" Vous avez attrapé un poisson !")
    else:
        print(" Rien hahaha...")
    player.decrease_stats()
