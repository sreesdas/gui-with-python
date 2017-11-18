import kivy
import math
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout

class MyBoxLayout(BoxLayout):
    pass

class CalcGridLayout(GridLayout):
    def calculate(self, calculation):
        if calculation:
            try:
                self.display.text = str(eval(calculation))
            except:
                self.display.text = "ERROR"

class Calculator(App):
    def build(self):
        return CalcGridLayout()


Calculator().run()
