"""
CP1404 Practical
Kivy GUI program to use dynamic labels
Nicola Culik
Started 10/11/2025
Estimate: 30 min
Actual: 13 min
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.core.window import Window

class DynamicLabelsApp(App):

    def build(self):
        """build the Kivy app from the kv file"""
        Window.size = (500, 300)
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.build_labels()
        return self.root

    def build_labels(self):
        """Build dynamic labels"""
        names = ["Nicola", "Bob", "Terry", "Test"]
        for name in names:
            temp_label = Label(text=name)
            self.root.ids.main.add_widget(temp_label)

DynamicLabelsApp().run()