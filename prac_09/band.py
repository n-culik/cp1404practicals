"""
Band class for CP1404
Author: Nicola Culik
"""


class Band:
    """Band class"""

    def __init__(self, name=""):
        """Construct a Band with a name and empty musician collection."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of a Band."""
        return f"{self.name} ({self.musicians})"

    def __repr__(self):
        """Return a string representation of a Band, showing the variables."""
        return str(vars(self))

    def add(self, musician):
        """Add an musician to musician's collection."""
        self.musicians.append(musician)

    def play(self):
        """Return a string showing the musician playing their first (or no) instrument."""
        for musician in self.musicians:
            if not musician.instruments:
                return f"{musician.name} needs an instrument!"
            else:
                return f"{musician.name} is playing: {musician.instruments[0]}"