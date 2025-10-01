"""
Module : CP1404
Date: 01.10.2025
Author: Nicola Culik
Description: Get some experience in file reading and writing
"""

"""
1.
Using write to ask the user for a name and create a new file with the name in it
"""
user_name = input("Enter your name: ")
file = open("name.txt", "w")
file.write(user_name)
file.close()
print()

"""
2.
Using read to get the name
"""
file = open("name.txt", "r")
name = file.read().strip()
print(f"Hi {name}!")
file.close()

"""
3.
Using with to open a file and get the first two numbers
"""
