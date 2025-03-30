class SkipHoistDigitalTwin:
    def __init__(self):
        self.skip = Skip(capacity=20.0, mass=5.0)
        self.drum = Drum(diameter=4.0, width=2.0, max_torque=50000)
        self.hoist_machine = HoistMachine(power=1000, max_speed=12.0)
        self.guides = ShaftGuides(length=1000.0)
        self.control_system = ControlSystem()

    def simulate_cycle(self, payload: float, travel_distance: float) -> None:
        if self.skip.load(payload):
            self.hoist_machine.release_brake()
            self.drum.set_speed(5.0)  # Примерная скорость
            self.control_system.update_position(travel_distance)
            print(f"Скип перемещен на {travel_distance} м")
            self.skip.unload()
            self.hoist_machine.apply_brake()
        else:
            print("Ошибка: перегруз скипа")

# Пример использования
twin = SkipHoistDigitalTwin()
twin.simulate_cycle(payload=15.0, travel_distance=500.0)
