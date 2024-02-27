from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    def __init__(self, weight: int | float = 0, fuel: int | float = 0, fuel_consumption: int | float = 0):
        self.weight = weight
        self.started = False
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self) -> None:
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError

    def move(self, distance: int | float) -> None:
        total_fuel = distance * self.fuel_consumption
        if total_fuel > self.fuel:
            raise NotEnoughFuel
        self.fuel -= total_fuel
