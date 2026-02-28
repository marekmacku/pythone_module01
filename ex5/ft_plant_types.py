class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def get_basic_info(self) -> str:
        return f"{self.height}cm, {self.age} days"


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int,
                 color: str) -> None:
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        print(f"{self.name} is blooming beautifully!")

    def get_info(self) -> str:
        return (f"{self.name} (Flower): {self.get_basic_info()}, "
                f"{self.color} color")


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int,
                 trunk_diameter: int) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        shade_area = int(self.height * 0.156)
        print(f"{self.name} provides {shade_area} square meters of shade")

    def get_info(self) -> str:
        return (f"{self.name} (Tree): {self.get_basic_info()}, "
                f"{self.trunk_diameter}cm diameter")


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int,
                 harvest_season: str, nutritional_value: str) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def get_info(self) -> str:
        return (f"{self.name} (Vegetable): {self.get_basic_info()}, "
                f"{self.harvest_season} harvest")

    def show_nutrition(self) -> None:
        print(f"{self.name} is rich in {self.nutritional_value}")


def main() -> None:
    print("=== Garden Plant Types ===")

    rose = Flower("Rose", 25, 30, "red")
    lily = Flower("Lily", 30, 40, "white")

    oak = Tree("Oak", 500, 1825, 50)
    pine = Tree("Pine", 600, 2000, 40)

    tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    carrot = Vegetable("Carrot", 25, 70, "autumn", "beta-carotene")

    plants = [rose, lily, oak, pine, tomato, carrot]

    for plant in plants:
        print(plant.get_info())

    rose.bloom()
    oak.produce_shade()
    tomato.show_nutrition()


if __name__ == "__main__":
    main()
