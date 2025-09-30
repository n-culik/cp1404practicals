"""
Module : CP1404
Date: 30.09.2025
Author: Nicola Culik
Description: In this file we will answer some questions about random
"""


# What did you see on line 1?
# What was the smallest number you could have seen, what was the largest?
# Answer: Smallest number is 5, largest is 20. It generates a random whole numbers between 5 and 20 inclusive

# What did you see on line 2?
# What was the smallest number you could have seen, what was the largest?
# Could line 2 have produced a 4?
# Answer: Smallest number is 3, largest is 9. It generates whole numbers between 3 and 10 but only the odd numbers. 4 would not be possible

# What did you see on line 3?
# What was the smallest number you could have seen, what was the largest?
# Answer: Smallest number is 2.5, largest is 5.5. It generates all decimal number between 2.5 and 5.5

# Write code, not a comment, to produce a random number between 1 and 100 inclusive.
import random
number = random.randint(1, 100)
print(number)