"""
CP1404 Practical
Display wimbledon winners and countries
Date: 16.10.2025
Author: Nicola Culik
Estimate: 60 min
Actual:   66 min
"""
import csv
FILENAME = "wimbledon.csv"

def main():
    wimbledon_winners = read_file(FILENAME)
    print("Wimbledon Champions:")
    print_winner_count(wimbledon_winners)
    print_country_winner(wimbledon_winners)

def read_file(filename):
    wimbledon_winners = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        reader = csv.reader(in_file)
        next(reader)
        for line in reader:
            wimbledon_winners.append(line)
    return wimbledon_winners

def print_winner_count(wimbledon_winners):
    winner_to_count = {}
    for winner in wimbledon_winners:
        winner = winner[2]
        try:
            winner_to_count[winner] += 1
        except KeyError:
            winner_to_count[winner] = 1
    for winner, count in winner_to_count.items():
        print(winner, count)

def print_country_winner(wimbledon_winners):
    countries = set()
    for country in wimbledon_winners:
        country = country[1]
        countries.add(country)
    print()
    print(f"These {len(countries)} countries have won Wimbledon:")
    print(", ".join(countries))


main()