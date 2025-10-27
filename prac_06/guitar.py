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
        return f"{self.name} ({self.year}) : ${self.cost}"


