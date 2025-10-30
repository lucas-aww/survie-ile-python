import random
from src.player import Player


def handle_random_event(player: Player):
    """
    Gère un événement aléatoire qui affecte le joueur.
    (Version simplifiée pour commencer)
    """
    print("\n--- Événement Aléatoire ---")

    events = ["pluie", "rencontre_animale", "decouverte_ressource"]
    chosen_event = random.choice(events)

    if chosen_event == "pluie":
        print("Une douce pluie tropicale commence à tomber...")
        player.soif = max(0, player.soif - 20)
        print("Votre soif diminue légèrement (-20).")

    elif chosen_event == "rencontre_animale":
        print("Vous rencontrez un animal.")
        # Simplification pour le moment, sans choix du joueur
        player.energie = max(0, player.energie - 10)
        print("Vous avez dû fuir, perdant 10 d'énergie.")

    elif chosen_event == "decouverte_ressource":
        print("Vous avez découvert des ressources.")
        player.faim = max(0, player.faim - 10)
        print("Votre faim diminue de 10.")

    print("---------------------------\n")
