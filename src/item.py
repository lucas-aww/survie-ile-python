class Item:
    def __init__(self, name, type, heal=0):
        self.name = name
        self.type = type
        self.heal = heal

    def use(self, player):
        if self.type == "potion":
            player.pv += self.heal
            print(f"🧪 Vous buvez une potion et regagnez {self.heal} PV !")
        elif self.type == "food":
            player.faim += self.heal
            player.fatigue -= 10
            print(f"🍖 Vous mangez {self.name} et regagnez {self.heal} points de faim.")
        elif self.type == "quest":
            print("🎁 Cet objet semble précieux...")
        else:
            print("❌ Vous ne pouvez pas utiliser cet objet.")
