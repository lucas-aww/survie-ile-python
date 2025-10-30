class Player:
    def __init__(self, faim=0, soif=0, energie=100):
        """
        Initialise un nouvel aventurier avec ses jauges vitales.
        0 = rassasié/hydraté, 100 = affamé/déshydraté (game over).
        100 = pleine énergie, 0 = épuisé (game over).
        """
        self.faim = faim
        self.soif = soif
        self.energie = energie

        print("Un nouvel aventurier est né sur l'île !")

    def __str__(self):
        """
        Représentation textuelle de l'état du joueur.
        """
        return (
            f"--- État de l'Aventurier ---\n"
            f"Faim    : {self.faim}/100 {'(Affamé !)' if self.faim >= 70 else ''}\n"
            f"Soif    : {self.soif}/100 {'(Déshydraté !)' if self.soif >= 70 else ''}\n"
            f"Énergie : {self.energie}/100 {'(Épuisé !)' if self.energie <= 30 else ''}\n"
            f"---------------------------"
        )


    def update_jauges_daily(self):
            """
            Met à jour les jauges du joueur pour une journée passée.
            Faim et Soif augmentent, Énergie diminue.
            Les jauges sont limitées entre 0 et 100.
            """
            print("\nLe jour passe... Les besoins vitaux se font sentir.")

            self.faim += 10
            self.soif += 15
            self.energie -= 10

            # Clamping des jauges pour rester dans les limites (0-100)
            self.faim = max(0, min(100, self.faim))
            self.soif = max(0, min(100, self.soif))
            self.energie = max(0, min(100, self.energie))

            print(
                f"Faim : +10 (actuel: {self.faim}), "
                f"Soif : +15 (actuel: {self.soif}), "
                f"Énergie : -10 (actuel: {self.energie})"
            )


    def is_game_over(self):
        """
        Vérifie si le jeu est terminé en raison de jauges critiques.
        """
        if self.faim >= 100:
            print("\nGAME OVER : Vous êtes mort de faim !")
            return True
        if self.soif >= 100:
            print("\nGAME OVER : Vous êtes mort de déshydratation !")
            return True
        if self.energie <= 0:
            print("\nGAME OVER : Vous êtes mort d'épuisement !")
            return True
        return False