from src.room import Room

def create_dungeon():
    entree = Room("Entrée", "Une grande porte de pierre marque le début du donjon.")
    couloir = Room("Couloir", "Un long couloir sombre et humide.")
    armurerie = Room("Armurerie", "Des armes anciennes reposent sur les murs.")
    foret = Room("Forêt du Donjon", "Une clairière à l'extérieur du donjon.", can_hunt=True)
    riviere = Room("Rivière", "Une rivière claire.", can_fish=True)
    tresor = Room("Salle du Trésor", "Le Trésor Sacré scintille dans la pénombre.")

    entree.connect("nord", couloir)
    couloir.connect("sud", entree)
    couloir.connect("est", armurerie)
    armurerie.connect("ouest", couloir)
    armurerie.connect("nord", foret)
    foret.connect("sud", armurerie)
    armurerie.connect("est", riviere)
    riviere.connect("ouest", armurerie)
    riviere.connect("nord", tresor)
    tresor.connect("sud", riviere)

    return entree, tresor
