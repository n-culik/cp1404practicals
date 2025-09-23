"""
Module : CP1404
Date: 23.09.2025
Author: Nicola Culik
Description: In this Program we will ask the user for a password and print it with asteriks
"""
MENU ="""(G)et a valid score (must be 0-100 inclusive)
(P)rint result (copy or import your function to determine the result from score.py)
(S)how stars (this should print as many stars as the score)
(Q)uit"""

def main():
    score = get_score()
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_score()
        elif choice == "P":
            pass
        elif choice == "S":
            pass
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("farewell")

def get_score():
    score = int(input("Enter your score: "))
    while score < 0 or score > 100:
        print("Invalid score. Please enter between 0-100 inclusive")
        score = int(input("Enter your score: "))
    return score

main()
