from goblin import Goblin
from hero import Hero


ARENA_NAME = "The Boiling Isles"

def battle(hero: Hero, enemy: Goblin):
    while hero.is_alive() and enemy.is_alive():
        hero_damage = hero.attack()
        enemy.take_damage(hero_damage)
        if enemy.is_alive():
            enemy_damage = enemy.attack()
            hero.take_damage(enemy_damage)

    if hero.is_alive():
        print(f"{hero.name} wins!")
    else:
        print(f"{enemy.name} wins!")


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
    battle(hero, goblin)


if __name__ == "__main__":
    main()
