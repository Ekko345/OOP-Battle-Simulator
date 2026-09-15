from goblin import Goblin
from hero import Hero


ARENA_NAME = "The Boiling Isles"


def main():
    """Open the arena and introduce its first opponent."""
    print(f"Welcome to {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The gates are opening...")

    goblin = Goblin("Luz")

    print(f"{goblin.name} enters the arena with {goblin.health} health.")


    NewGoblin = Goblin("amity")
    
    print(f"{NewGoblin.name} enters the arena with {NewGoblin.health} health.")

    hero=Hero("King", 100, 20)
    print("A hero approaches the arena...")
    print(f"{hero.name} enters the arena with {hero.health} health and {hero.attack_power} attack power.")

    goblin_damage = goblin.attack()
    print(f"{goblin.name} attacks {hero.name} for {goblin_damage} damage.")

    hero.take_damage(goblin_damage)

    if __name__ == "__main__":
        main()
