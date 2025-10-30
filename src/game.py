def start_game():
    player = Player()
    current_room, treasure_room = create_dungeon()

    player.clear_screen()
    print("🏕️ Bienvenue dans le jeu de survie !")
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
            print("👋 Vous quittez le jeu.")
            break

        else:
            print("Commande inconnue.")

        # Combat automatique
        for enemy in current_room.enemies:
            if not enemy.is_dead():
                enemy.attack(player)
                if player.pv <= 0:
                    print("💀 Vous êtes mort. Défaite.")
                    return

        # Fin de journée après chaque tour
        player.next_day()

    # Victoire si le joueur a survécu 12 jours
    if player.pv > 0 and player.jour > 12:
        print("🏆 Félicitations ! Vous avez survécu 12 jours ! Victoire !")
    elif player.pv <= 0:
        print("💀 Vous êtes mort avant la fin des 12 jours. Défaite.")
