class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.plant_age = age

    """Formatted getter for all of the attributes"""
    def get_info(self) -> str:
        return f"{self.name}: {self.height}cm, {self.plant_age} days old"

    def grow(self, gain: int) -> None:
        self.height += gain

    def age(self, days: int) -> None:
        self.plant_age += days


def main() -> None:
    rose = Plant("Rose", 25, 30)
    print("=== Day 1 ===")
    print(rose.get_info())

    days_to_simulate = 6
    growth_per_week = 6

    rose.grow(growth_per_week)
    rose.age(days_to_simulate)

    print(f"=== Day {days_to_simulate} ===")
    print(rose.get_info())
    print(f"Growth this week: +{growth_per_week}cm")


if __name__ == "__main__":
    main()
