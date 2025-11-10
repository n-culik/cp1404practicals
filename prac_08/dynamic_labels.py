"""
CP1404 Practical
Kivy GUI program to use dynamic labels
Nicola Culik
Started 10/11/2025
Estimate: 30 min
Actual:  min
"""

from kivy.app import App
from kivy.lang import Builder

class DynamicLabelsApp(App):
    def build(self):
        """ build the Kivy app from the kv file """
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        return self.root

DynamicLabelsApp().run()