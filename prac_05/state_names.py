"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
Date: 15.10.2025
"""
CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania", "SA": "South Australia"}


for code, name in CODE_TO_NAME.items():
    print(f"{code:3} is {name}")

state_code = input("Enter short state: ").upper()

while state_code != "":
    is_valid = False
    while not is_valid:
        try:
            print(state_code, "is", CODE_TO_NAME[state_code])
            is_valid = True
        except KeyError:
            print("Invalid short state")
        state_code = input("Enter short state: ").upper()
        if state_code == "":
            is_valid = True