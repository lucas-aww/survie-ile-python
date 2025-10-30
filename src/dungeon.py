from src.room import Room

def create_dungeon():
    entree = Room("Entrée", "Début du donjon.")
    couloir = Room("Couloir", "Un long couloir sombre.")
    armurerie = Room("Armurerie", "Vieilles armes.", can_hunt=False, can_fish=False)
    foret = Room("Forêt du Donjon", "Endroit idéal pour chasser.", can_hunt=True)
    riviere = Room("Rivière", "Endroit idéal pour pêcher.", can_fish=True)
    tresor = Room("Salle du Trésor", "Le Trésor Sacré scintille ici.")

    entree.connect("nord", couloir)
    couloir.connect("sud", entree)
    couloir.connect("est", armurerie)
    couloir.connect("nord", foret)
    foret.connect("sud", couloir)
    foret.connect("est", riviere)
    riviere.connect("ouest", foret)
    armurerie.connect("est", tresor)
    tresor.connect("ouest", armurerie)

    return entree, tresor
