class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.items = []
        self.enemies = []

    def connect(self, direction, room):
        self.connections[direction] = room

    def show_info(self):
        print(f"\n📍 Vous êtes dans {self.name}")
        print(self.description)
        if self.items:
            print("Objets présents :", ", ".join([i.name for i in self.items]))
        if self.enemies:
            print("Ennemis :", ", ".join([e.name for e in self.enemies]))
        print("Sorties :", ", ".join(self.connections.keys()))
