import random


class Hero:
    """The hero blueprint will be implemented later in the project."""
    def __init__(self, name, health, attack_power):
        health = random.randint(100, 150)
        attack_power = random.randint(10, 25)
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self):
        return self.attack_power
    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
        print(f"{self.name} takes {damage} damage. Health: {self.health}")

    def is_alive(self):
        return self.health > 0