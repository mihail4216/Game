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

    def __init__(self):
        super(RapLayout, self).__init__()
        self.count1=0
    # def pig(self):
    #     popup = Popup(title="popup",content=Label(text='you pig'),size_hint=(None,None),auto_dismiss=True,size=(400,400))
    #     popup.open()
    def t_random_word(self):
        i = random.randint(1, 28221)


        return dicture()[i]


    def count(self,a):

        a+=1
        return a

    def check(self,x,y):
        upper_rifma = y.upper()
        slovo = x.lower()
        rifma = y.lower()
        # print upper_rifma

        if rifma.encode('utf-8') in dicture():
            if slovo[-2:2]==rifma[-2:2]:

                self.display.text=''
                # self.t_random_word()
                return 1
        return 0






class MyRapApp(App):

    def build(self):
        return RapLayout()

    def on_pause(self):
        return True

    def on_resume(self):
        pass


if __name__ == '__main__':
    app=MyRapApp()
    app.run()