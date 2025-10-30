from src.player import Player
from src.dungeon import create_dungeon

def start_game():
    player = Player()
    current_room, treasure_room = create_dungeon()

    print("🏰 Bienvenue dans le Donjon du Trésor Sacré !")
    current_room.show_info()

    while player.pv > 0:
        action = input("\nQue voulez-vous faire ? (aller / utiliser / quitter) : ").lower()

        if action == "aller":
            direction = input("Direction ? (nord / sud / est / ouest) : ").lower()
            if direction in current_room.connections:
                current_room = current_room.connections[direction]
                current_room.show_info()
            else:
                print("🚫 Impossible d'aller par là.")

        elif action == "utiliser":
            item_name = input("Quel objet ? ")
            for item in player.inventory:
                if item.name.lower() == item_name.lower():
                    item.use(player)
                    break
            else:
                print("❌ Objet introuvable dans votre inventaire.")

        elif action == "quitter":
            print("👋 Vous quittez le donjon.")
            break

        else:
            print("Commande inconnue.")

        # Combat automatique si ennemis présents
        for enemy in current_room.enemies:
            if not enemy.is_dead():
                enemy.attack(player)
                if player.pv <= 0:
                    print("💀 Vous êtes mort. Défaite.")
                    return

        # Condition de victoire
        if current_room == treasure_room:
            for item in current_room.items:
                if item.name == "Trésor Sacré":
                    print("🏆 Vous avez trouvé le Trésor Sacré ! Victoire !")
                    return
