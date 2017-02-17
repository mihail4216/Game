# -*- coding: utf-8 -*-
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
Builder.load_file('calc.kv')

class ClacLayout(GridLayout):

    # def pig(self):
    #     popup = Popup(title="popup",content=Label(text='you pig'),size_hint=(None,None),auto_dismiss=True,size=(400,400))
    #     popup.open()

    def Calculate(self,calculation):
        if calculation:
            try:
                self.display.text=str(eval(calculation))
            except Exception:
                self.display.text= "Error"




class MyApp(App):

    def build(self):
        return ClacLayout()

    def on_pause(self):
        return True

    def on_resume(self):
        pass


if __name__ == '__main__':
    MyApp().run()