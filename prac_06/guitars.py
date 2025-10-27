"""
CP1404 Practical
Email name extraction
Date: 27.10.2025
Author: Nicola Culik
Estimate: 50 min
Actual:   min
"""

from guitar import Guitar

def main():
    guitars = []
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    for i, guitar in enumerate(guitars, 1):
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}")


main()