"""
CP1404/CP5632 - Practical
Program to determine score status
"""
import random

def main():
    score = float(input("Enter score: "))
    result = validate_score(score)
    print(f"your score is {result}")

    random_score = random.randint(0, 100)
    result = validate_score(random_score)
    print(f"Your score is {result}")


def validate_score(score: float):
    if score < 0 or score > 100:
        result = "Invalid score"
    elif score >= 90:
        result = "Excellent"
    elif score >= 50:
        result = "Passable"
    else:
        result = "Bad"
    return result

main()