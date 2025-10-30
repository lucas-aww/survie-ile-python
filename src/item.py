class Item:
    def __init__(self, name, type_, heal=0):
        self.name = name
        self.type = type_
        self.heal = heal

    def use(self, player):
        if self.type == "food":
            player.faim += self.heal
            print(f" Vous mangez {self.name} et restaurez {self.heal} de faim.")
            if player.faim > 100:
                player.faim = 100
        elif self.type == "drink":
            player.soif += self.heal
            print(f" Vous buvez {self.name} et restaurez {self.heal} de soif.")
            if player.soif > 100:
                player.soif = 100
                
