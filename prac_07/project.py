"""
CP1404 Practical
Project class
Date: 04.11.2025
Author: Nicola Culik
Estimate: 40 min
Actual:  23 min
"""

class Project:
    """Project class"""

    def __init__(self, name = "", start_date = "", priority = 0, cost = 0.0, completion_percent = 0 ):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost = cost
        self.completion_percent = completion_percent

    def __str__(self):
        formatted_date = self.start_date.strftime("%d/%m/%Y")
        return f"{self.name}, start: {formatted_date}, priority: {self.priority}, estimate: ${self.cost:.2f}, completion: {self.completion_percent}%"

    def __lt__(self, other):
        """Return True if priority is lower than other priority of a project"""
        return self.priority < other.priority

    def is_complete(self):
        """Return True if project is complete"""
        if self.completion_percent == 100:
            return True
        else:
            return False