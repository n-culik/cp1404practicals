"""
CP1404 Practical
Silver service Taxi class
Author: Nicola Culik
"""

from taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised version of a Taxi that includes flagfall and fanciness."""
    flagfall = 4.50

    def __init__(self, name = "", fuel = 0, fanciness = 0.0):
        """Initialise a SilverServiceTaxi instance, based on parent class Taxi."""
        super().__init__(name, fuel)
        self.price_per_km = Taxi.price_per_km * fanciness

    def __str__(self):
        """Return a string like a Taxi but with current flagfall."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"

