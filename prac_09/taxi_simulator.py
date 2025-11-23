"""
Taxi simulator code for CP1404
Author: Nicola Culik
Date: 23.11.2025
"""
from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi
MENU = """q)uit, c)hoose taxi, d)rive"""

def main():
    current_taxi = None
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_bill = 0.0
    print("Let's drive!")
    print(MENU)
    choice = input(">>>").upper()
    while choice != "Q":
        if choice == "C":
            print("Taxis available:")
            display_taxis(taxis)
            current_taxi = choose_taxi(taxis)
            display_bill(current_bill)
        elif choice == "D":
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
                display_bill(current_bill)
            else:
                display_taxi_fare(current_taxi)
                current_bill += current_taxi.get_fare()
                display_bill(current_bill)
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>>").upper()
    print(f"Total trip cost: ${current_bill:.2f}")
    print("Taxis are now")
    display_taxis(taxis)

def display_taxis(taxis):
    i = 0
    for taxi in taxis:
        print(f"{i} - {taxi}")
        i += 1

def choose_taxi(taxis):
    taxi_choice = validate_number_input("Choose taxi:")
    try:
        taxis[taxi_choice]
        return taxis[taxi_choice]
    except IndexError:
        print("Invalid taxi choice")

def validate_number_input(menu_title):
    """Validates the user input for numbers"""
    is_valid = False
    while not is_valid:
        try:
            taxi_choice = int(input(f"{menu_title} "))
            is_valid = True
        except ValueError:
            print("Please enter a valid number")
    return taxi_choice

def display_bill(current_fare):
    print(f"Bill to date: ${current_fare:.2f}")

def display_taxi_fare(current_taxi):
    drive_distance = validate_number_input("Drive how far?")
    current_taxi.drive(drive_distance)
    print(f"Your {current_taxi.name} trip cost you ${current_taxi.get_fare()}")


main()