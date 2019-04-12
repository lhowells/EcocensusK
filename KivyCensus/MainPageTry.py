import kivy
kivy.require('1.9.0') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.button import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput


class EcoCensus(App):

    def build(self):
        return FloatLayout()

if __name__ == '__main__':
    EcoCensus().run()