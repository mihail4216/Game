# -*- coding: utf-8 -*-
import random
from paserer import dicture
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
Builder.load_file('rap.kv')

class RapLayout(GridLayout):

    # def pig(self):
    #     popup = Popup(title="popup",content=Label(text='you pig'),size_hint=(None,None),auto_dismiss=True,size=(400,400))
    #     popup.open()
    def t_random_word(self):
        i = random.randint(1, 28221)


        return dicture()[i]



    def check(self,):
        # print 'display '+self.
        print 'displayid' + self.display['ver']
        pass



class MyRapApp(App):

    def build(self):
        return RapLayout()

    def on_pause(self):
        return True

    def on_resume(self):
        pass


if __name__ == '__main__':
    MyRapApp().run()