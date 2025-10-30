import os
import random

class Player:
    def __init__(self):
        self.pv = 100
        self.faim = 50
        self.soif = 50
        self.fatigue = 30
        self.jour = 1
        self.inventaire = []
        self.vivant = True
        self.current_room = None  
        

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def show_stats(self):
        print(f"\nPV: {self.pv} | Faim: {self.faim}/100 | Soif: {self.soif}/100 | Énergie: {100 - self.fatigue}/100 | Jour: {self.jour}/12")

    def show_inventory(self):
        if self.inventaire:
            print("\nInventaire :", ", ".join(self.inventaire))
        else:
            print("\nInventaire vide.")

    def use_item(self, item_name):
        if item_name in self.inventaire:
            if item_name == "poisson":
                self.faim = max(0, self.faim - 20)
                print("Vous mangez un poisson et réduisez votre faim.")
            elif item_name == "fruit":
                self.faim = max(0, self.faim - 15)
                self.soif = max(0, self.soif - 10)
                print("Vous mangez un fruit juteux. Faim et soif diminuent.")
            elif item_name == "eau":
                self.soif = max(0, self.soif - 30)
                print("Vous buvez de l’eau fraîche.")
            self.inventaire.remove(item_name)
        else:
            print("Objet introuvable dans l’inventaire.")

    def rest(self):
        if self.faim < 50 and self.soif < 50:
            self.fatigue = max(0, self.fatigue - 40)
            self.faim += 10
            self.soif += 10
            print("Vous vous reposez et regagnez de l’énergie.")
            self.next_day()
        else:
            print("Vous avez trop faim ou trop soif pour dormir.")

    def decrease_stats(self):
        self.faim = min(100, self.faim + random.randint(3, 7))
        self.soif = min(100, self.soif + random.randint(4, 8))
        self.fatigue = min(100, self.fatigue + random.randint(5, 10))

        if self.faim >= 100 or self.soif >= 100 or self.fatigue >= 100:
            self.pv -= 20
            print("⚠️ Vos conditions se dégradent...")

        if self.pv <= 0:
            self.vivant = False

    def next_day(self):
        self.jour += 1
        self.decrease_stats()
        if self.jour > 12:
            print("\n Félicitations ! Vous avez survécu 12 jours !")
            self.vivant = False
