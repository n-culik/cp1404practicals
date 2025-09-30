"""
CP1404/CP5632 - Practical
Date: 30.09.2025
Answer the following questions:
1. When will a ValueError occur?
When I enter a string like a letter or special character or an float number into either the numerator or denominator.
2. When will a ZeroDivisionError occur?
When I enter 0 into the denominator
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Yes, one could check for the user input 0
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Denominator cannot be zero")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")