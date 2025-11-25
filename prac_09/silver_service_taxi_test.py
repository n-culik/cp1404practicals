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

    sst2 = SilverServiceTaxi("Taxi", 100, 2)
    sst2.drive(18)
    assert sst2.get_fare() == 48.80, f"Expected 48.80, got {sst2.get_fare():.2f}"
    print(f"{sst2.get_fare():.2f}")

main()