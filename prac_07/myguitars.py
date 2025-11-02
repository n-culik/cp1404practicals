"""
CP1404 Practical
Guitar code
Date: 02.11.2025
Author: Nicola Culik
Estimate: 50 min
Actual:   min
"""
from guitar import Guitar
FILENAME = "guitars.csv"

def main():
    guitars = []

    data = open_file()
    for line in data:
        parts = line.strip().split(',')
        year = int(parts[1])
        price = float(parts[2])
        guitar = Guitar(parts[0], year, price)
        guitars.append(guitar)

    guitars.sort()
    for guitar in guitars:
        print(guitar)


def open_file():
    with open(FILENAME, "r") as in_file:
        data = in_file.readlines()
    return data


main()