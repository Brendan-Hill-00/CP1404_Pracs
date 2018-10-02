"""
CP1404/CP5632 Practical
Unreliable Car class
"""
from prac_08.car import Car
from random import randint


class UnreliableCar(Car):
    """Specialised version of a Car that includes reliability."""

    def __init__(self, name, fuel, reliability):
        """Initialise a Taxi instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def __str__(self):
        return "{}, fuel={}, odometer={}".format(self.name, self.fuel, self.odometer)

    def drive(self, distance):
        if randint(0, 100) < self.reliability:
            distance_driven = super().drive(distance)
            return distance_driven
