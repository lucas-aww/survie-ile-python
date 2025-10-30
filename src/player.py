import os

class Player:
    def __init__(self):
        self.pv = 100
        self.faim = 100
        self.fatigue = 0
        self.jour = 1
        self.inventory = []

    def show_stats(self):
        print(f"PV: {self.pv} | Faim: {self.faim} | Fatigue: {self.fatigue} | Jour: {self.jour}/12")

    def clear_screen(self):
        os.system("cls" if os.name == "nt" else "clear")

    def decrease_stats(self, action_type="general"):
        # Faim
        if action_type in ["general", "chasser", "pecher"]:
            self.faim -= 5
        # Fatigue
        if action_type in ["general", "aller", "chasser", "pecher"]:
            self.fatigue += 10
        # PV si faim ou fatigue critique
        if self.faim <= 0:
            self.pv -= 10
        if self.fatigue >= 100:
            self.pv -= 5

        self.faim = max(0, min(self.faim, 100))
        self.fatigue = max(0, min(self.fatigue, 100))

    def rest(self):
        if self.faim < 50:
            print(" Vous êtes trop affamé pour vous reposer !")
            return False
        print(" Vous vous reposez et réduisez votre fatigue.")
        self.fatigue -= 30
        self.fatigue = max(0, self.fatigue)
        self.next_day()
        return True

    def next_day(self):
        self.jour += 1
        self.faim -= 10
        self.fatigue += 5
        if self.faim <= 0:
            self.pv -= 10
        if self.fatigue >= 100:
            self.pv -= 5
        self.faim = max(0, self.faim)
        self.fatigue = min(100, self.fatigue)
