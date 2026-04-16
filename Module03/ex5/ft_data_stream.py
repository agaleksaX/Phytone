import random
from typing import Generator

print("=== Game Data Stream Processor ===")


def gen_event() -> Generator[tuple, None, None]:
    players = ["alice", "bob", "charlie", "dylan"]
    actions = [
        "run",
        "eat",
        "sleep",
        "grab",
        "move",
        "climb",
        "swim",
        "release",
        "use",
    ]
    while True:
        yield (random.choice(players), random.choice(actions))


def consume_event(events: list) -> Generator[tuple, None, None]:
    while len(events) > 0:
        index = random.randrange(len(events))
        event = events.pop(index)
        yield event


stream = gen_event()

for i in range(1000):
    name, action = next(stream)
    print(f"Event {i}: Player {name} did action {action}")

events = [next(stream) for _ in range(10)]
print(f"Built list of 10 events: {events}")

for event in consume_event(events):
    print(f"Got event from list: {event}")
    print(f"Remains in list: {events}")
