"""
CP1404- Practical
In this program we get to learn different for loops
"""

"""
This is the for loop from the practical as an example
"""
for i in range(1, 21, 2):
    print(i, end=' ')
print()

"""
This is the for loop for question A
count in 10s from 0 to 100
"""
for i in range(0, 101, 10):
    print(i, end=' ')
print()

"""
This is the for loop for question B
count down from 20 to 1
"""
for i in range(20, 0, -1):
    print(i, end=' ')
print()

"""
This is the for loop for question C
print n stars. Ask the user for a number, then print that many stars (*), all on one line.
"""
number_of_stars = int(input("How many stars do you want? "))
for i in range(number_of_stars):
    print("*", end='')
print()

"""
This is the for loop for question D
print n lines of increasing stars. Using the same number as above, print lines of increasing stars, starting at 1 with no blank line
"""
for i in range(1, number_of_stars+1):
    print("*" * i)
print()