import random
from enemy import Enemy

class Boss(Enemy):
    """A completed character class students can examine as an OOP example."""

    def __init__(self, name):
        super().__init__(name, 200)
        self.attack_power = 20
        self.gold=0

    def stealGold(self, hero):
        """Return a random amount of damage."""
        self.gold+=hero.gold
        hero.gold=0
        print("GET RECK NOOB")

