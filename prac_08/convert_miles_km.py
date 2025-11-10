"""
CP1404 Practical
Kivy GUI program to convert miles to km
Nicola Culik
Started 10/11/2025
Estimate: 50 min
Actual:  0 min
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

class ConvertMilesKm(App):
    """ ConvertMilesKmApp is a Kivy App for converting miles to km """
    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (500, 300)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

ConvertMilesKm().run()