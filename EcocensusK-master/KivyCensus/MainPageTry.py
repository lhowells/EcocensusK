import kivy
import os
kivy.require('1.9.0') # replace with your current kivy version !
from tkinter import filedialog
from tkinter import *
from kivy.app import App
from kivy.uix.button import Label , Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput

import image_partition as impa
import predictions as predict
import imageReader as imread

class Layout(FloatLayout):
    def selectDirectory(self):
        Tk().withdraw()
        self.folder.text = filedialog.askdirectory()
        # need to figure out how kivys file thing works
    def Predict(self):
        Folder = self.folder.text
        altitude = float(self.altitude.text)
        threshold = float(self.threshold.text)
        impa.main(Folder)
        predict.main(Folder, threshold)
        imread.main(Folder, altitude)
        partdirectory = os.path.dirname(Folder + '/Partitions/')
        os.rmdir(partdirectory)

class EcoCensus(App):

    def build(self):
        return Layout()

if __name__ == '__main__':
    EcoCensus().run()