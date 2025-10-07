"""
Module : CP1404
Date: 07.10.2025
Author: Nicola Culik
Description: Get some experience with lists
"""
import random

NUMBER_PER_LINE = 6
MIN = 1
MAX = 45

def main():
    number_of_quick_picks = int(input("How many quick picks? "))

    for i in range(0, number_of_quick_picks):
        quick_picks = []
        for j in range(0, NUMBER_PER_LINE):
            random_number = random.randint(MIN, MAX)
            while random_number in quick_picks:
                random_number = random.randint(MIN, MAX)
            quick_picks.append(random_number)
        quick_picks.sort()
        print(" ".join(f"{number:2}" for number in quick_picks))
main()