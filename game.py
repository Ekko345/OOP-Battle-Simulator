from goblin import Goblin


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
    print("But no hero has answered the call... yet.")


if __name__ == "__main__":
    main()
