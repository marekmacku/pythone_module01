class Plant:
    def __init__(self, name: str, height: int) -> None:
        self.name = name
        self.height = height

    def grow(self, gain: int) -> None:
        self.height += gain
        print(f"{self.name} grew {gain}cm")

    def get_info(self) -> str:
        return f"{self.name}: {self.height}cm"


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, color: str,
                 blooming_state: str) -> None:
        super().__init__(name, height)
        self.color = color
        self.blooming_state = blooming_state

    def bloom(self) -> None:
        self.blooming_state = True
        print(f"{self.name} is blooming beautifully!")

    def get_info(self) -> str:
        status = "blooming" if self.blooming_state else "not blooming"
        return f"{self.name}: {self.height}cm, {self.color} flowers ({status})"


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, color: str,
                 blooming_state: str, prize_points: int) -> None:
        super().__init__(name, height, color, blooming_state)
        self.prize_points = prize_points
