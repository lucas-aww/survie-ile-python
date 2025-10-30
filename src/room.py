from src.ascii_art import ROOM_ART

class Room:
    def __init__(self, name, description, can_hunt=False, can_fish=False):
        self.name = name
        self.description = description
        self.connections = {}
        self.items = []
        self.can_hunt = can_hunt
        self.can_fish = can_fish

    def connect(self, direction, room):
        self.connections[direction] = room

    def show_info(self):
        art = ROOM_ART.get(self.name, "")
        if art:
            print(art)
        print(f"\nVous êtes dans {self.name}")
        print(self.description)
        if self.items:
            print("Objets présents :", ", ".join([i.name for i in self.items]))
        print("Sorties :", ", ".join(self.connections.keys()))
        if self.can_hunt:
            print("Vous pouvez chasser ici.")
        if self.can_fish:
            print("Vous pouvez pêcher ici.")
