class Player:
    def __init__(self):
        self.pv = 100
        self.faim = 100
        self.soif = 100
        self.fatigue = 0
        self.inventory = []
        self.jour = 1  # Nouveau : jour actuel

    def show_stats(self):
        print(f"\n📅 Jour: {self.jour}/12 | ❤️ PV: {self.pv} | 🍗 Faim: {self.faim} | 💧 Soif: {self.soif} | 😴 Fatigue: {self.fatigue}")

    def next_day(self):
        self.jour += 1
        print(f"\n🌅 Le jour {self.jour} commence...")
        # Décrémentation quotidienne
        self.faim -= 10
        self.soif -= 5
        self.fatigue += 10
        if self.faim <= 0 or self.soif <= 0 or self.fatigue >= 100:
            self.pv -= 15
            print("⚠️ Vous souffrez des conditions de survie !")
        # Limites
        self.faim = max(0, min(self.faim, 100))
        self.soif = max(0, min(self.soif, 100))
        self.fatigue = max(0, min(self.fatigue, 100))
