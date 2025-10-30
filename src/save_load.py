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


def load_game():
    """
    Charge une partie sauvegardée à partir du fichier JSON.
    Retourne une instance de Player et le numéro du jour,
    ou (None, None) si la sauvegarde n'existe pas ou est invalide.
    """
    try:
        with open(SAVE_FILE, 'r') as f:
            save_data = json.load(f)

        # Vérifier que toutes les clés nécessaires sont présentes
        required_keys = ["faim", "soif", "energie", "day_count"]
        if all(key in save_data for key in required_keys):
            player = Player(
                faim=save_data["faim"],
                soif=save_data["soif"],
                energie=save_data["energie"]
            )
            day_count = save_data["day_count"]
            print(f"\nPartie chargée depuis {SAVE_FILE} !")
            return player, day_count
        else:
            print("Fichier de sauvegarde corrompu ou incomplet. Démarrage d'une nouvelle partie.")
            return None, None

    except FileNotFoundError:
        print(f"Aucune partie sauvegardée trouvée ({SAVE_FILE}). Démarrage d'une nouvelle partie.")
        return None, None
    except json.JSONDecodeError:
        print(
            f"Erreur de lecture du fichier de sauvegarde ({SAVE_FILE}). Le fichier n'est pas un JSON valide. Démarrage d'une nouvelle partie.")
        return None, None
    except Exception as e:
        # Capturer d'autres exceptions inattendues
        print(f"Une erreur inattendue est survenue lors du chargement : {e}. Démarrage d'une nouvelle partie.")
        return None, None