class Enemy:
    def __init__(self, name, pv, damage):
        self.name = name
        self.pv = pv
        self.damage = damage

    def attack(self, player):
        print(f"{self.name} attaque {player.name} !")
        player.take_damage(self.damage)

    def is_dead(self):
        return self.pv <= 0
