"""
CP1404 Practical
Email name extraction
Date: 27.10.2025
Author: Nicola Culik
Estimate: 20 min
Actual:   min
"""

class Guitar:
    def __init__(self, name="", year=0, cost=0.0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:.2f}"

    def get_age(self):
        actual_year = 2025
        self.age = actual_year - self.year
        return self.age

    def is_vintage(self):
        if self.get_age() >= 50:
            return True
        else:
            return False
