class Drum:
    def __init__(self, diameter: float, width: float, max_torque: float):
        self.diameter = diameter  # Диаметр барабана, м
        self.width = width        # Ширина барабана, м
        self.max_torque = max_torque  # Максимальный крутящий момент, Н·м
        self.angular_velocity = 0.0  # Угловая скорость, рад/с

    def set_speed(self, speed: float) -> None:
        self.angular_velocity = speed
