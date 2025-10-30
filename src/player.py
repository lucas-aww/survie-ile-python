import os

class Player:
    def __init__(self):
        self.pv = 100
        self.faim = 100
        self.soif = 100
        self.fatigue = 0
        self.inventory = []
        self.jour = 1

    def add_item(self, item):
        self.inventory.append(item)
        print(f" {item.name} ajouté à l'inventaire.")

    def show_inventory(self):
        if not self.inventory:
            print("Votre inventaire est vide.")
        else:
            print(" Inventaire :", ", ".join([item.name for item in self.inventory]))

    def show_stats(self):
        print(f"\n Jour: {self.jour}/12 |  PV: {self.pv} |  Faim: {self.faim} |  Soif: {self.soif} |  Fatigue: {self.fatigue}")

    def next_day(self):
        self.jour += 1
        print(f"\n Le jour {self.jour} commence...")
        self.faim -= 10
        self.soif -= 5
        self.fatigue += 10
        if self.faim <= 0 or self.soif <= 0 or self.fatigue >= 100:
            self.pv -= 15
            print(" Vous souffrez des conditions de survie !")
        self.faim = max(0, min(self.faim, 100))
        self.soif = max(0, min(self.soif, 100))
        self.fatigue = max(0, min(self.fatigue, 100))

    def rest(self):
        print(" Vous vous reposez et réduisez votre fatigue.")
        self.fatigue -= 20
        if self.fatigue < 0:
            self.fatigue = 0

    def decrease_stats(self):
        self.faim -= 5
        self.fatigue += 5
        if self.faim <= 0 or self.fatigue >= 100:
            self.pv -= 10

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
