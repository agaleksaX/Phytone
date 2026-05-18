from ex0 import AquaFactory, FlameFactory
from ex0.creature import Creature, CreatureFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import BattleStrategy
from ex2 import AggressiveStrategy, DefensiveStrategy, NormalStrategy

Opponent = tuple[CreatureFactory, BattleStrategy]


def battle(first: Opponent, second: Opponent) -> None:

    first_factory, first_strategy = first
    second_factory, second_strategy = second

    first_creature = first_factory.create_base()
    second_creature = second_factory.create_base()

    print("* Battle *")

    print(first_creature.describe())
    print("vs.")
    print(second_creature.describe())

    print("now fight!")

    first_strategy.act(first_creature)
    second_strategy.act(second_creature)
