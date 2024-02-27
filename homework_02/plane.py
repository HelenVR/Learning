"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


class Plane(Vehicle):
    def __init__(self, weight: int | float = 0,
                 fuel: int | float = 0,
                 fuel_consumption: int | float = 0,
                 max_cargo: int = 0):
        super().__init__(weight, fuel, fuel_consumption)
        self.cargo = 0
        self.max_cargo = max_cargo

    def load_cargo(self, weight: int | float) -> None:
        if self.cargo + weight > self.max_cargo:
            raise CargoOverload

        self.cargo += weight

    def remove_all_cargo(self) -> int | float:
        weight = self.cargo
        self.cargo = 0
        return weight
