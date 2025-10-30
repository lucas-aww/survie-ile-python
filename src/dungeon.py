from src.room import Room
from src.item import Item
from src.enemy import Enemy

def create_dungeon():
    # Création des pièces
    entree = Room("Entrée", "Une grande porte de pierre marque le début du donjon.")
    couloir = Room("Couloir", "Un long couloir sombre et humide.")
    epreuve = Room("Salle des Épreuves", "Des pièges et des énigmes à résoudre.")
    armurerie = Room("Armurerie", "Des armes anciennes reposent sur les murs.")
    tresor = Room("Salle du Trésor", "Le Trésor Sacré scintille dans la pénombre.")

    # Connexions
    entree.connect("nord", couloir)
    couloir.connect("sud", entree)
    couloir.connect("est", epreuve)
    epreuve.connect("ouest", couloir)
    epreuve.connect("nord", armurerie)
    armurerie.connect("sud", epreuve)
    armurerie.connect("est", tresor)
    tresor.connect("ouest", armurerie)

    # Objets
    armurerie.items.append(Item("Épée", "weapon"))
    epreuve.items.append(Item("Potion", "potion", 30))
    tresor.items.append(Item("Trésor Sacré", "quest"))

    # Ennemis
    couloir.enemies.append(Enemy("Gobelin", 20, 10))
    epreuve.enemies.append(Enemy("Squelette", 30, 15))

    return entree, tresor
