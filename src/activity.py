import random
from src.item import Item

def hunt(player):
    print("🏹 Vous partez chasser...")
    success = random.random() < 0.6
    if success:
        meat = Item("Viande", "food", heal=20)
        player.add_item(meat)
        print("🦌 Vous avez chassé avec succès et obtenu de la viande !")
    else:
        print("🐾 Vous n'avez rien trouvé cette fois...")
    player.decrease_stats()


def fish(player):
    print("🎣 Vous tentez de pêcher...")
    success = random.random() < 0.5
    if success:
        fish = Item("Poisson", "food", heal=15)
        player.add_item(fish)
        print("🐟 Vous avez attrapé un poisson !")
    else:
        print("🌊 Rien n’a mordu à l’hameçon...")
    player.decrease_stats()
