from src.player import Player
from src.dungeon import create_dungeon
from src.activity import hunt, fish

def start_game():
    player = Player()
    current_room, treasure_room = create_dungeon()

    player.clear_screen()
    print(" Bienvenue dans le jeu de survie !")
    current_room.show_info()

    while player.pv > 0 and player.jour <= 12:
        player.show_stats()
        action = input("\nQue voulez-vous faire ? (aller / utiliser / inventaire / chasser / pecher / se_reposer / quitter) : ").lower()
        player.clear_screen()

        if action == "aller":
            direction = input("Direction ? (nord / sud / est / ouest) : ").lower()
            if direction in current_room.connections:
                current_room = current_room.connections[direction]
                current_room.show_info()
            else:
                print(" Impossible d'aller par là.")
            player.decrease_stats()

        elif action == "utiliser":
            item_name = input("Quel objet ? ")
            for item in player.inventory:
                if item.name.lower() == item_name.lower():
                    item.use(player)
                    player.inventory.remove(item)
                    break
            else:
                print(" Objet introuvable dans votre inventaire.")
            player.decrease_stats()

        elif action == "inventaire":
            player.show_inventory()

        elif action == "chasser":
            hunt(player, current_room)

        elif action == "pecher":
            fish(player, current_room)

        elif action == "se_reposer":
            player.rest()

        elif action == "quitter":
            print(" Vous quittez le jeu.")
            break

        else:
            print("Commande inconnue.")

        # Fin de journée
        player.next_day()

    if player.pv > 0 and player.jour > 12:
        print(" Félicitations ! Vous avez survécu 12 jours ! Victoire !")
    elif player.pv <= 0:
        print(" Vous êtes mort avant la fin des 12 jours. Défaite.")
