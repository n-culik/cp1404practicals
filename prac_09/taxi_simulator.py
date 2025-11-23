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
    print("Let's drive!")
    print(MENU)
    choice = input(">>>").upper()
    while choice != "Q":
        if choice == "C":
            print("Taxis available:")
            display_taxis(taxis)
            choose_taxi(taxis)
        elif choice == "D":
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                pass
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>>").upper()
    print("Taxis are now")
    display_taxis(taxis)

def display_taxis(taxis):
    i = 0
    for taxi in taxis:
        print(f"{i} - {taxi}")
        i += 1



main()