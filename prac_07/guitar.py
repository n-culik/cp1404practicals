"""
CP1404 Practical
Guitar class
Date: 02.11.2025
Author: Nicola Culik
Estimate: 0 min
Actual:  0 min
"""
class Guitar:
    """Guitar class"""

    def __init__(self, name="", year=0, cost=0.0):
        """Construct a Guitar from the given values"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return string representation of a Guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:.2f}"

    def __lt__(self, other):
        """Return True if year of Guitar is less than year of other Guitar."""
        return self.year < other.year

    def get_age(self):
        """Return age of Guitar."""
        actual_year = 2025
        self.age = actual_year - self.year
        return self.age

    def is_vintage(self):
        """Return True if Guitar is vintage."""
        if self.get_age() >= 50:
            return True
        else:
            return False