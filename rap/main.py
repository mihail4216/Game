# -*- coding: utf-8 -*-
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
Builder.load_file('rap.kv')

class RapLayout(GridLayout):
    def qwe(self):
        pass


class RapApp(App):

    def build(self):
        ui=RapLayout()
        return ui

    def on_pause(self):
        return True

    def on_resume(self):
        pass

if __name__ == '__main__':

    RapApp().run()
