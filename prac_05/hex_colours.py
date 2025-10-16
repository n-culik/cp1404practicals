"""
CP1404 Practical
Color names and codes in a dictionary
User input for color name to get color code
Date: 15.10.2025
Author: Nicola Culik
"""
NAME_TO_CODE = {'Amaranth': '#e52b50', 'Amber': '#ffbf00', 'Amethyst': '#9966cc',
                'Aqua': '#00ffff', 'Asparagus': '#87a96b', 'Baby Blue': '#89cff0',
                'Beaver': '#9f8170', 'Beige': '#f5f5dc', 'Bistre': '#3d2b1f', 'Black': '#000000'}
max_name_length = max(len(name) for name in list(NAME_TO_CODE.keys()))

for name, code in NAME_TO_CODE.items():
    print(f"{name:{max_name_length}} is {code}")

color_name = input('Enter the name of the color: ').title()
while color_name != "":
    is_valid = False
    while not is_valid:
        try:
            print(color_name, "is", NAME_TO_CODE[color_name])
            is_valid = True
        except KeyError:
            print("Invalid color name")
        color_name = input("Enter the name of the color: ").title()
        if color_name == "":
            is_valid = True

