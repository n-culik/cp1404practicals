"""
CP1404 Practical
Guitar code
Date: 02.11.2025
Author: Nicola Culik
Estimate: 50 min
Actual:  24 min
"""
from guitar import Guitar
FILENAME = "guitars.csv"

def main():
    guitars = open_file()
    print("Your current guitars are:")
    guitars.sort()
    print_guitar(guitars)
    print()

    print("Add a new guitar")
    name = input("Name of the guitar:")
    while name !="":
        year = int(input("Year of guitar:"))
        price = float(input("Price of guitar:"))
        guitars.append(Guitar(name, year, price))
        name = input("Name of new guitar:")

    print()
    print("Your new guitars are:")
    guitars.sort()
    print_guitar(guitars)

    write_file(guitars)

def print_guitar(guitars):
    for guitar in guitars:
        print(guitar)

def open_file():
    guitars = []
    with open(FILENAME, "r") as in_file:
        for line in in_file:
            parts = line.strip().split(',')
            year = int(parts[1])
            price = float(parts[2])
            guitar = Guitar(parts[0], year, price)
            guitars.append(guitar)
    return guitars

def write_file(guitars):
    with open(FILENAME, "w") as out_file:
        for guitar in guitars:
            csv_data = f"{guitar.name},{guitar.year},{guitar.cost}\n"
            out_file.write(f"{csv_data}")

main()