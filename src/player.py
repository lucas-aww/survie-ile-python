import os

class Player:
    def __init__(self):
        self.pv = 100
        self.faim = 100
        self.soif = 100
        self.fatigue = 0
        self.inventory = []

    def show_stats(self):
        print(f"\n❤️ PV: {self.pv} | 🍗 Faim: {self.faim} | 💧 Soif: {self.soif} | 😴 Fatigue: {self.fatigue}")

    def add_item(self, item):
        self.inventory.append(item)
        print(f"🎒 Vous avez obtenu : {item.name}")

    def use_item(self, item_name):
        for item in self.inventory:
            if item.name.lower() == item_name.lower():
                item.use(self)
                self.inventory.remove(item)
                return
        print("❌ Objet introuvable.")

    def show_inventory(self):
        print("\n🎒 Inventaire :")
        if not self.inventory:
            print("Votre inventaire est vide.")
        else:
            for i, item in enumerate(self.inventory, 1):
                print(f"{i}. {item.name} ({item.type})")

    def decrease_stats(self):
        """Décrémente les jauges à chaque action."""
        self.faim -= 5
        self.soif -= 3  # on ne peut pas encore boire, mais la soif diminue lentement
        self.fatigue += 5

        if self.faim <= 0 or self.soif <= 0 or self.fatigue >= 100:
            self.pv -= 10
            print("⚠️ Vous souffrez du manque de ressources !")

        # bornes
        self.faim = max(0, min(self.faim, 100))
        self.soif = max(0, min(self.soif, 100))
        self.fatigue = max(0, min(self.fatigue, 100))

    def rest(self):
        """Permet de se reposer pour récupérer de la fatigue et un peu de PV."""
        print("😴 Vous vous reposez un moment...")
        self.fatigue = max(0, self.fatigue - 30)
        self.pv = min(100, self.pv + 10)
        print("💤 Vous vous sentez reposé.")
        self.decrease_stats()

    @staticmethod
    def clear_screen():
        """Nettoie la console (Windows, Linux, Mac)."""
        os.system('cls' if os.name == 'nt' else 'clear')
