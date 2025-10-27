"""
CP1404 Practical
Email name extraction
Date: 27.10.2025
Author: Nicola Culik
Estimate: 30 min
Actual:   min
"""
from guitar import Guitar

guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
print(guitar.get_age())
print(guitar.is_vintage())
print(guitar)