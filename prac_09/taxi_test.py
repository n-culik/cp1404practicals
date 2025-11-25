"""
CP1404 Practical
Taxi class test code
Author: Nicola Culik
"""

from taxi import Taxi

def main():
    my_taxi = Taxi("Prius 1", 100)
    print(my_taxi)
    my_taxi.drive(40)
    print(my_taxi)
    print(f"Current fare: ${my_taxi.get_fare():.2f}")
    print("New fare")
    my_taxi.start_fare()
    my_taxi.drive(100)
    print(my_taxi)
    print(f"Current fare: ${my_taxi.get_fare():.2f}")
main()