class Item:
    def __init__(self, name, type_, value=0):
        self.name = name
        self.type = type_
        self.value = value

    def use(self, player):
        if self.type == "potion":
            player.heal(self.value)
            print(f"{player.name} utilise une potion et récupère {self.value} PV !")
        elif self.type == "weapon":
            print(f"{player.name} brandit {self.name} avec détermination.")
        elif self.type == "quest":
            print(f"{player.name} contemple le {self.name}.")
