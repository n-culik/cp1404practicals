"""
CP1404 Practical
Taxi class test code
Author: Nicola Culik
"""

from unreliable_car import UnreliableCar

def main():
    ur_car1 = UnreliableCar("Car 1", 1000, 90)
    ur_car2 = UnreliableCar("Car 2", 1000, 40)

    for i in range(0, 50):
        print("New drive")
        print(ur_car1)
        print(ur_car2)
        ur_car1.drive(20)
        ur_car2.drive(88)

main()

