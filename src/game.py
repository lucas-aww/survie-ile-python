import random
from src.player import Player
from src.activity import hunt, fish
from src.room import create_dungeon

def random_event(player):
    event = random.choice(["pluie", "fruit", "rencontre", "rien"])

    if event == "pluie":
        print("\n Il pleut aujourd’hui, votre soif diminue un peu.")
        player.soif = max(0, player.soif - 20)

    elif event == "fruit":
        print("\n Vous trouvez un arbre fruitier !")
        player.inventaire.append("fruit")

    elif event == "rencontre":
        print("\n Vous croisez un animal sauvage !")
        choix = input("Voulez-vous le chasser (o/n) ? ").lower()
        if choix == "o":
            resultat = random.choice(["réussite", "échec"])
            if resultat == "réussite":
                print("Vous avez chassé avec succès.")
                player.inventaire.append("viande")
            else:
                print("L’animal vous blesse légèrement.")
                player.pv -= 10
        else:
            print("Vous décidez de fuir. Vous perdez un peu d’énergie.")
            player.fatigue += 10

    else:
        print("\nRien d’inhabituel aujourd’hui.")

def start_game():
    player = Player()
    current_room, _ = create_dungeon()

    player.clear_screen()
    print("Bienvenue sur l’île déserte !")
    current_room.show_info()

    while player.vivant and player.jour <= 12:
        player.show_stats()
        print("\nSorties :", ", ".join(current_room.connections.keys()))
        action = input("\nAction ? (aller / inventaire / chasser / pecher / utiliser / se_reposer / explorer / quitter) : ").lower()
        player.clear_screen()

        if action == "aller":
            direction = input("Direction ? (nord/sud/est/ouest) : ").lower()
            if direction in current_room.connections:
                current_room = current_room.connections[direction]
                current_room.show_info()
                player.decrease_stats()
            else:
                print("Impossible d'aller par là.")

        elif action == "inventaire":
            player.show_inventory()

        elif action == "utiliser":
            item_name = input("Quel objet ? ")
            player.use_item(item_name)

        elif action == "chasser":
            hunt(player)

        elif action == "pecher":
            fish(player)

        elif action == "explorer":
            random_event(player)
            player.decrease_stats()

        elif action == "se_reposer":
            player.rest()

        elif action == "quitter":
            print("Fin de partie.")
            break

        else:
            print("Commande inconnue.")

    print("\n Fin du jeu. Merci d’avoir joué !")
