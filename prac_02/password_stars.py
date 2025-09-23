"""
Module : CP1404
Date: 23.09.2025
Author: Nicola Culik
Description: In this Program we will ask the user for a password and print it with asteriks
"""
MIN_PASSWORD_LENGTH = 8
SPECIAL_CHARACTER = "*"

def main():
    user_password = get_password()
    print_password(user_password)


def print_password(user_password: str):
    print(SPECIAL_CHARACTER * len(user_password))


def get_password() -> str:
    user_password = input("Please enter a password: ")
    while len(user_password) < MIN_PASSWORD_LENGTH:
        print(f"Password must be at least {MIN_PASSWORD_LENGTH} characters long")
        user_password = input("Please enter a password: ")
    return user_password


main()
