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