class ShaftGuides:
    def __init__(self, length: float, material: str = "steel"):
        self.length = length    # Длина направляющих, м
        self.material = material
        self.wear_level = 0.0  # Уровень износа (0-1)

    def update_wear(self, delta: float) -> None:
        self.wear_level = min(1.0, max(0.0, self.wear_level + delta))
