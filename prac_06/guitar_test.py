"""
CP1404 Practical
Email name extraction
Date: 27.10.2025
Author: Nicola Culik
Estimate: 30 min
Actual:  16 min
"""
from guitar import Guitar

guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
guitar2 = Guitar("Another Guitar", 2013, 435.50)
print(f"{guitar.name} get_age() - Expected 103. Got {guitar.get_age()}")
print(f"{guitar2.name} get_age() - Expected 12. Got {guitar2.get_age()}")
print(f"{guitar.name} is_vintage() - Expected Ture. Got {guitar.is_vintage()}")
print(f"{guitar2.name} is_vintage() - Expected False. Got {guitar2.is_vintage()}")
print(guitar)
print(guitar2)