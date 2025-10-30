from src.player import Player
from src.dungeon import create_dungeon
from src.activity import hunt, fish

def start_game():
    player = Player()
    current_room, treasure_room = create_dungeon()

    print("🏰 Bienvenue dans le Donjon du Trésor Sacré !")
    current_room.show_info()

    while player.pv > 0:
        player.show_stats()
        action = input("\nQue voulez-vous faire ? (aller / utiliser / chasser / pecher / quitter) : ").lower()

        if action == "aller":
            direction = input("Direction ? (nord / sud / est / ouest) : ").lower()
            if direction in current_room.connections:
                current_room = current_room.connections[direction]
                current_room.show_info()
            else:
                print("🚫 Impossible d'aller par là.")
            player.decrease_stats()

        elif action == "utiliser":
            item_name = input("Quel objet ? ")
            player.use_item(item_name)
            player.decrease_stats()

        elif action == "chasser":
            hunt(player)

        elif action == "pecher":
            fish(player)

        elif action == "quitter":
            print("👋 Vous quittez le donjon.")
            break

        else:
            print("Commande inconnue.")

        # Vérifie la mort du joueur
        if player.pv <= 0:
            print("💀 Vous êtes mort. Défaite.")
            return

        # Condition de victoire
        if current_room == treasure_room:
            for item in current_room.items:
                if item.name == "Trésor Sacré":
                    print("🏆 Vous avez trouvé le Trésor Sacré ! Victoire !")
                    return
