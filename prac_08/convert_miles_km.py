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

MILES = 1.609344

class ConvertMilesKm(App):
    """ ConvertMilesKmApp is a Kivy App for converting miles to km """
    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (500, 300)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def convert_miles_km(self):
        """Convert miles to km"""
        value = float(self.root.ids.input_number.text)
        result = value * MILES
        self.root.ids.output_result.text = str(result)

    def handle_increment(self, value):
        """Update the user input by up/down 1 of its value"""
        new_value = float(self.root.ids.input_number.text) + value
        self.root.ids.input_number.text = str(new_value)


ConvertMilesKm().run()