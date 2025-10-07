"""
Module : CP1404
Date: 07.10.2025
Author: Nicola Culik
Description: Get some experience with lists
"""

numbers = [3, 1, 4, 1, 5, 9, 2]

"""
Values to the questions:
numbers[0] -> 3
numbers[-1] -> 2
numbers[3] -> 1
numbers[:-1] -> [3, 1, 4, 1, 5 ,9 ,2]
numbers[3:4] -> [1]
5 in numbers -> True
7 in numbers -> False
"3" in numbers ->  False
numbers + [6, 5, 3] -> Extends the list with 6, 5, 3 -> [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
"""

numbers[0] = "ten"

numbers[-1] = 1

print(numbers[2:])
if 9 in numbers:
    print("9 is in numbers")
