class HoistMachine:
    def __init__(self, power: float, max_speed: float, brake_type: str = "disc"):
        self.power = power          # Мощность двигателя, кВт
        self.max_speed = max_speed  # Макс. скорость подъема, м/с
        self.brake_type = brake_type  # Тип тормоза
        self.is_brake_applied = False

    def apply_brake(self) -> None:
        self.is_brake_applied = True

    def release_brake(self) -> None:
        self.is_brake_applied = False
