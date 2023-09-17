from dataclasses import dataclass, field
from typing import List


@dataclass
class Car:
    make: str
    model: str
    year: int
    fuel_efficiency: float
    speed: int
    price: float


@dataclass
class Sedan(Car):
    trunk_capacity: int


@dataclass
class SUV(Car):
    cargo_capacity: int


class MockData:
    @staticmethod
    def cars() -> List[Car]:
        return [
            Sedan("Toyota", "Camry", 2022, 30.5, 140, 25_000, 15),
            Sedan("Honda", "Civic", 2023, 32.0, 135, 24_000, 14),
            Sedan("Ford", "Escape", 2022, 25.0, 150, 28_000, 16),
            SUV("Chevrolet", "Tahoe", 2023, 18.0, 110, 42_000, 80),
            SUV("Jeep", "Wrangler", 2023, 20.0, 120, 35_000, 60),
            SUV("Ford", "Explorer", 2022, 22.5, 130, 38_000, 70)
        ]


@dataclass
class TaxiPark:
    __cars: List[Car] = field(default_factory=MockData.cars, init=False)

    def calculate_fleet_cost(self):
        return sum(car.price for car in self.__cars)

    def sort_by_fuel_efficiency(self):
        return sorted(self.__cars, key=lambda car: car.fuel_efficiency)

    def get_cars_by_speed(self, min_speed, max_speed):
        return [car for car in self.__cars if min_speed <= car.speed <= max_speed]


taxi_park = TaxiPark()

total_cost = taxi_park.calculate_fleet_cost()
sorted_cars = taxi_park.sort_by_fuel_efficiency()
cars_by_speed = taxi_park.get_cars_by_speed(min_s := 130, max_s := 150)

print(f"-> Стоимость парка:\n{total_cost:,.0f} р")

print("\n-> Сортировка по расходу топлива:")
[print(f"{car.make} {car.model} ({car.fuel_efficiency} л/100 км)") for car in sorted_cars]

print(f"\n-> Фильтр по скорости ({min_s}-{max_s} км/ч):")
[print(f"{car.make} {car.model} ({car.speed} км/ч)") for car in cars_by_speed]
