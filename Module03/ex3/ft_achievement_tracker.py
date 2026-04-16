import random


def gen_player_achievements(all_achievements: list[str]) -> set[str]:
    count = random.randint(3, len(all_achievements))
    return set(random.sample(all_achievements, count))


if __name__ == "__main__":
    print("=== Achievement Tracker System ===\n")

    all_achievements = [
        "Crafting Genius",
        "World Savior",
        "Master Explorer",
        "Collector Supreme",
        "Untouchable",
        "Boss Slayer",
        "Strategist",
        "Speed Runner",
        "Survivor",
        "Treasure Hunter",
        "First Steps",
        "Sharp Mind",
        "Unstoppable",
        "Hidden Path Finder"
    ]

    players = {
        "Alice": gen_player_achievements(all_achievements),
        "Bob": gen_player_achievements(all_achievements),
        "Charlie": gen_player_achievements(all_achievements),
        "Dylan": gen_player_achievements(all_achievements),
    }

    for name, achievements in players.items():
        print(f"Player {name}: {achievements}")

    all_unique = set().union(*players.values())
    print(f"\nAll distinct achievements: {all_unique}")

    common = set.intersection(*players.values())
    print(f"\nCommon achievements: {common}\n")

    for name, achievements in players.items():
        others = set().union(
            *(players[n] for n in players if n != name)
        )
        only = achievements - others
        print(f"Only {name} has: {only}")

    print()
    full_set = set(all_achievements)
    for name, achievements in players.items():
        missing = full_set - achievements
        print(f"{name} is missing: {missing}")
