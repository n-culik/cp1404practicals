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
    print(wimbledon_winners)
    winner_to_count = count_winner(wimbledon_winners)
    print(winner_to_count)
    # print_wimbledon_winners(wimbledon_winners)

def read_file(filename):
    wimbledon_winners = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        for line in in_file:
            wimbledon_winners.append(line.split(","))
    return wimbledon_winners

def count_winner(wimbledon_winners):
    winner_to_count = {}
    for winner in wimbledon_winners:
        winner = winner[2]
        try:
            winner_to_count[winner] += 1
        except KeyError:
            winner_to_count[winner] = 1
    return winner_to_count

# def print_wimbledon_winners(wimbledon_winners):
#     for winner in wimbledon_winners:



main()