"""
Module : CP1404
Date: 22.09.2025
Author: Nicola Culik
Description: In this Program we will ask the user for a password and print it with asteriks
"""
import getpass

MIN_PASSWORD_LENGTH = 8
SPECIAL_CHARACTER = "*"

def main():
    user_password = input("Please enter a password: ")
    while len(user_password) < MIN_PASSWORD_LENGTH:
        print(f"Password must be at least {MIN_PASSWORD_LENGTH} characters long")
        user_password = input("Please enter a password: ")
    print(SPECIAL_CHARACTER * len(user_password))

main()
