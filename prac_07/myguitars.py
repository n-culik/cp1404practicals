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
        guitar = Guitar(parts[0], parts[1], parts[2])
        guitars.append(guitar)


def open_file():
    with open(FILENAME, "r") as in_file:
        data = in_file.readlines()
    return data


main()