

## 🧙‍♂️ `src/player.py`


class Player:
    def __init__(self, name="Tom", pv=100):
        self.name = name
        self.pv = pv
        self.inventory = []

    def add_item(self, item):
        self.inventory.append(item)
        print(f"{self.name} a obtenu {item}.")

    def take_damage(self, amount):
        self.pv -= amount
        print(f"{self.name} subit {amount} dégâts. PV restants : {self.pv}")
        if self.pv <= 0:
            print(f"{self.name} est mort...")

    def heal(self, amount):
        self.pv += amount
        print(f"{self.name} récupère {amount} PV. PV actuels : {self.pv}")
