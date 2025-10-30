from src.player import Player
from src.dungeon import create_dungeon
from src.activity import hunt, fish

def start_game():
    player = Player()
    current_room, treasure_room = create_dungeon()
    player.current_room = current_room

    player.clear_screen()
    print("🏕️ Bienvenue dans le jeu de survie !")
    current_room.show_info()

    while player.pv > 0 and player.jour <= 12:
        player.show_stats()
        action = input("\nAction ? (aller / inventaire / chasser / pecher / utiliser / se_reposer / quitter) : ").lower()
        player.clear_screen()

        day_over = False

        if action == "aller":
            direction = input("Direction ? (nord/sud/est/ouest) : ").lower()
            if direction in current_room.connections:
                current_room = current_room.connections[direction]
                player.current_room = current_room
                current_room.show_info()
            else:
                print("🚫 Impossible d'aller par là.")
            player.decrease_stats("aller")

        elif action == "inventaire":
            print("Inventaire :", [i.name for i in player.inventory])

        elif action == "chasser":
            hunt(player)
            player.decrease_stats("chasser")

        elif action == "pecher":
            fish(player)
            player.decrease_stats("pecher")

        elif action == "utiliser":
            item_name = input("Objet à utiliser ? ")
            # placeholder pour utiliser item
            print(f"Vous utilisez {item_name}")
            player.decrease_stats("general")

        elif action == "se_reposer":
            day_over = player.rest()

        elif action == "quitter":
            print("👋 Vous quittez le jeu.")
            break

        else:
            print("Commande inconnue.")

        if day_over:
            print(f"📅 Fin de la journée {player.jour-1}. Jour suivant : {player.jour}/12")

        if current_room == treasure_room:
            print("🏆 Vous avez trouvé le Trésor Sacré ! Victoire !")
            break

    if player.pv <= 0:
        print("💀 Vous êtes mort avant la fin des 12 jours. Défaite.")

