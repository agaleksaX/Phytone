# ft_plant_types.py

class Plant:
    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.age} days old")


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str):
        super().__init__(name, height, age)
        self.color = color
        self._bloomed = False

    def bloom(self) -> None:
        self._bloomed = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if self._bloomed:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int, trunk_diameter: float):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(f"Tree {self.name} now produces a shade of "
              f"{self.height}cm long and {self.trunk_diameter}cm wide.")

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}cm")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int, harvest_season: str):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = 0

    def grow(self, days: int) -> None:
        self.age += days
        self.height += days * 2.1   # чтобы высота росла правильно
        self.nutritional_value += days

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")


# ===================== Главная программа =====================
if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    
    print("=== Flower")
    f = Flower("Rose", 15.0, 10, "red")
    f.show()
    print("[asking the rose to bloom]")
    f.bloom()
    f.show()
    
    print( )
    print("=== Tree")
    t = Tree("Oak", 200.0, 365, 5.0)
    t.show()
    print("[asking the oak to produce shade]")
    t.produce_shade()
    
    print( )
    print("=== Vegetable")
    v = Vegetable("Tomato", 5.0, 10, "April")
    v.show()
    print("[make tomato grow and age for 20 days]")
    v.grow(20)
    v.show()