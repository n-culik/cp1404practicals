"""
CP1404 Practical
Silver service Taxi class test code
Author: Nicola Culik
"""
from silver_service_taxi import SilverServiceTaxi

def main():
    sst = SilverServiceTaxi("Hummer", 200, 4)
    print(sst)

    sst.drive(20)
    print(sst)
    print(sst.get_fare())


main()