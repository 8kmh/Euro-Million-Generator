from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty

import random

class BoxLayoutTest(BoxLayout):

    randomlist = []
    complementarylist = []
    numero = StringProperty("Bonne Chance")
    numerocomplementaire = StringProperty("")

    def on_button_click(self):
        self.randomlist = random.sample(range(1, 50), 5) 
        self.complementarylist = random.sample(range(1, 12), 2)
        self.randomlist.sort()
        self.complementarylist.sort()
        self.numero = str(self.randomlist)
        self.numerocomplementaire = str(self.complementarylist)

class EuroMillionGeneratorApp(App):
    pass


EuroMillionGeneratorApp().run()