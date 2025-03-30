class ControlSystem:
    def __init__(self):
        self.current_speed = 0.0
        self.target_speed = 0.0
        self.position = 0.0     # Текущая позиция скипа в стволе, м

    def update_speed(self, new_speed: float) -> None:
        self.current_speed = new_speed

    def update_position(self, delta: float) -> None:
        self.position += delta
