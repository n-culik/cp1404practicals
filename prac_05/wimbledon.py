"""
CP1404 Practical
Display wimbledon winners and countries
Date: 16.10.2025
Author: Nicola Culik
Estimate: 60 min
Actual:   min
"""
FILENAME = "wimbledon.csv"

def main():
    wimbledon_winners = read_file(FILENAME)

def read_file(filename):
    wimbledon_winners = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        for line in in_file:
            wimbledon_winners.append(line.split(","))
main()