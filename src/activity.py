from random import randint
from src.ascii_art import HUNT_ART, FISH_ART

def hunt(player):
    if not player.current_room.can_hunt:
        print(" Vous ne pouvez pas chasser ici.")
        return
    print(HUNT_ART)
    success = randint(0, 1)
    if success:
        print("Vous avez chassé avec succès ! Faim +20")
        player.faim += 20
    else:
        print("Vous n'avez rien attrapé.")
    player.faim = min(player.faim, 100)

def fish(player):
    if not player.current_room.can_fish:
        print(" Vous ne pouvez pas pêcher ici.")
        return
    print(FISH_ART)
    success = randint(0, 1)
    if success:
        print("Vous avez pêché un poisson ! Faim +15")
        player.faim += 15
    else:
        print("Vous n'avez rien attrapé.")
    player.faim = min(player.faim, 100)
