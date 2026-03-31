class Plant:
    class Stats:
        def __init__(self) -> None:
            self.grow_calls = 0
            self.age_calls = 0
            self.show_calls = 0

        def display(self) -> None:
            print(f"Stats: {self.grow_calls} grow, "
                  f"{self.age_calls} age, {self.show_calls} show")

    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._height = height
        self._age = age
        self._stats = Plant.Stats()

    def grow(self) -> None:
        self._height += 5.0
        self._stats.grow_calls += 1

    def age_up(self) -> None:
        self._age += 1
        self._stats.age_calls += 1

    def show(self) -> None:
        print(f"{self._name}: {self._height}cm, {self._age} days old")
        self._stats.show_calls += 1

    def get_stats(self) -> "Plant.Stats":
        return self._stats

    @staticmethod
    def is_older_than_year(age: int) -> bool:
        return age > 365

    @classmethod
    def anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
        self._bloomed = False

    def bloom(self) -> None:
        self._bloomed = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if self._bloomed:
            print(f"{self._name} is blooming beautifully!")
        else:
            print(f"{self._name} has not bloomed yet")


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int,
                 trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        self._shade_calls = 0

    def produce_shade(self) -> None:
        print(f"Tree {self._name} now produces a shade of "
              f"{self._height}cm long and {self.trunk_diameter}cm wide.")
        self._shade_calls += 1

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}cm")

    def get_shade_stats(self) -> int:
        return self._shade_calls


class Seed(Flower):
    def __init__(self, name: str, height: float, age: int,
                 color: str) -> None:
        super().__init__(name, height, age, color)
        self.seeds = 0

    def bloom(self) -> None:
        super().bloom()
        self.seeds = 42

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self.seeds}")


def show_stats(plant: Plant) -> None:
    stats = plant.get_stats()
    stats.display()

    if isinstance(plant, Tree):
        print(f"{plant.get_shade_stats()} shade")


if __name__ == "__main__":
    print("=== Garden statistics ===")

    print("=== Check year-old ===")
    print("Is 30 days more than a year? ->",
          Plant.is_older_than_year(30))
    print("Is 400 days more than a year? ->",
          Plant.is_older_than_year(400))

    print("\n=== Flower ===")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    print("[statistics for Rose]")
    show_stats(rose)

    print("[asking the rose to grow and bloom]")
    rose.grow()
    rose.bloom()
    rose.show()
    print("[statistics for Rose]")
    show_stats(rose)

    print("\n=== Tree ===")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    print("[statistics for Oak]")
    show_stats(oak)

    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print("[statistics for Oak]")
    show_stats(oak)

    print("\n=== Seed ===")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    sunflower.show()

    print("[make sunflower grow, age and bloom]")
    sunflower.grow()
    sunflower.age_up()
    sunflower.bloom()
    sunflower.show()

    print("[statistics for Sunflower]")
    show_stats(sunflower)

    print("\n=== Anonymous ===")
    unknown = Plant.anonymous()
    unknown.show()
    print("[statistics for Unknown plant]")
    show_stats(unknown)
