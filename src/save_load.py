import json
from src.player import Player

SAVE_FILE = "savegame.json"

def save_game(player: Player, day_count: int):
    """
    Sauvegarde l'état actuel du joueur et le numéro du jour dans un fichier JSON.
    """
    save_data = {
        "faim": player.faim,
        "soif": player.soif,
        "energie": player.energie,
        "day_count": day_count,
    }
    try:
        with open(SAVE_FILE, 'w') as f:
            json.dump(save_data, f, indent=4)
        print(f"\nPartie sauvegardée dans {SAVE_FILE} !")
    except IOError as e:
        print(f"Erreur lors de la sauvegarde : {e}")

# La fonction load_game sera ajoutée ensuite