class Skip:
    def __init__(self, capacity: float, mass: float, material: str = "steel"):
        self.capacity = capacity  # Грузоподъемность, тонн
        self.mass = mass          # Масса скипа, тонн
        self.material = material  # Материал конструкции
        self.is_loaded = False   # Загружен ли скип

    def load(self, payload: float) -> bool:
        if payload <= self.capacity:
            self.is_loaded = True
            return True
        return False

    def unload(self) -> None:
        self.is_loaded = False
