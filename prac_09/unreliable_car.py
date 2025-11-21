"""
CP1404 Practical
unreliable car class
Author: Nicola Culik
"""

import random
from car import Car



class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        drive_probability = random.randint(0, 1)
        if drive_probability < self.reliability:
            distance_driven = super().drive(distance)
        return distance_driven


