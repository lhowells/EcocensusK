import kivy
import os
kivy.require('1.9.0') # replace with your current kivy version !
from tkinter import filedialog
from tkinter import *
from kivy.app import App
from kivy.uix.button import Label , Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from PIL import Image
import image_partition as impa
import predictions as predict
import imageReader as imread

class bidirectional_iterator(object):
    def __init__(self, collection):
        self.collection = collection
        self.index = 0

    def next(self):
        try:
            result = self.collection[self.index]
            self.index += 1
        except IndexError:
            raise StopIteration
        return result

    def prev(self):
        self.index -= 1
        if self.index < 0:
            raise StopIteration
        return self.collection[self.index]

    def __iter__(self):
        return self

class Layout(FloatLayout):
    imglist =[]
    def selectDirectory(self):
        Tk().withdraw()
        self.folder.text = filedialog.askdirectory()
        print (self.folder.text)
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
        self.Imglist()

    def Imglist(self):
        directory = os.listdir(self.folder.text)
        imglist = []
        for file in directory:
            if ".JPG" in file or ".jpg" in file:
                imglist.append(Image.open( self.folder.text +"/"+ file))
        self.imglist = bidirectional_iterator(imglist)

    def next(self):
        if self.imglist == []:
            return
        im = Image(source = self.imglist.next())
        self.canvas.Rectangle.source = im
        im.reload
        return self.imglist.next()

    def prev(self):
        if self.imglist == []:
            return
        im = Image(source=self.imglist.prev())
        self.canvas.Rectangle.source = im
        im.reload
        return self.imglist.prev()


#class LineRectangle(Widget):
    #pass

class EcoCensus(App):

    def build(self):
        #FloatLayout.add_widget(LineRectangle(self, Widget))
        return Layout()

if __name__ == '__main__':
    EcoCensus().run()
