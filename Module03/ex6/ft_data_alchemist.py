import random

players = [
    "Alice",
    "bob",
    "Charlie",
    "dylan",
    "Emma",
    "Gregory",
    "john",
    "kevin",
    "Liam",
]

capitalized = [name.capitalize() for name in players]

only_capitalized = [name for name in players if name[0].isupper()]

scores = {name: random.randint(0, 1000) for name in capitalized}

avg = sum(scores.values()) / len(scores)

high_scores = {name: score for name, score in scores.items() if score > avg}

print("=== Game Data Alchemist ===\n")
print(f"Initial list of players: {players}")
print(f"New list with all names capitalized: {capitalized}")
print(f"New list of capitalized names only: {only_capitalized}\n")
print(f"Score dict: {scores}")
print(f"Score average is {round(avg, 2)}")
print(f"High scores: {high_scores}")
