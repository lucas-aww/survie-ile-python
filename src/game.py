from src.player import Player
from src.dungeon import create_dungeon
from src.activity import hunt, fish

def start_game():
    player = Player()
    current_room, treasure_room = create_dungeon()

    player.clear_screen()
    print("🏰 Bienvenue dans le Donjon du Trésor Sacré !")
    current_room.show_info()

    while player.pv > 0:
        player.show_stats()
        action = input("\nQue voulez-vous faire ? (aller / utiliser / inventaire / chasser / pecher / se_reposer / quitter) : ").lower()
        player.clear_screen()

        if action == "aller":
            direction = input("Direction ? (nord / sud / est / ouest) : ").lower()
            if direction in current_room.connections:
                current_room = current_room.connections[direction]
                player.clear_screen()
                current_room.show_info()
            else:
                print("🚫 Impossible d'aller par là.")
            player.decrease_stats()

        elif action == "utiliser":
            item_name = input("Quel objet ? ")
            player.use_item(item_name)
            player.decrease_stats()

        elif action == "inventaire":
            player.show_inventory()

        elif action == "chasser":
            hunt(player)

        elif action == "pecher":
            fish(player)

        elif action == "se_reposer":
            player.rest()

        elif action == "quitter":
            print("👋 Vous quittez le donjon.")
            break

        else:
            print("Commande inconnue.")

        # Vérifie la mort
        if player.pv <= 0:
            print("💀 Vous êtes mort. Défaite.")
            return

        # Condition de victoire
        if current_room == treasure_room:
            for item in current_room.items:
                if item.name == "Trésor Sacré":
                    print("🏆 Vous avez trouvé le Trésor Sacré ! Victoire !")
                    return
