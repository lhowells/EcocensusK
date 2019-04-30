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
import kivy.uix.image as Kimage
import image_partition as impa
import predictions as predict
import imageReader as imread
from kivy.graphics import *
from kivy.properties import StringProperty
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Color
from kivy.base import EventLoop



class bidirectional_iterator(object):
    def __init__(self, collection):
        self.collection = collection
        self.index = 0
    def next(self):
        self.index += 1
        if self.index == len(self.collection):
            self.index = self.index - 1
            return self.collection[self.index]
        result = self.collection[self.index]
        return result

    def prev(self):
        self.index -= 1
        if self.index < 0:
            self.index = 0
            return self.collection[self.index]
        result = self.collection[self.index]
        return result

    def __iter__(self):
        return self

class Layout(FloatLayout):
    imglist =[]

   # def update(self, imdir):
    #    self.rect.source = imdir
    def selectDirectory(self):
        Tk().withdraw()
        self.folder.text = filedialog.askdirectory()
        #print (self.folder.text)
        directory = os.listdir(self.folder.text)
        imglist = []
        for file in directory:
            if ".JPG" in file or ".jpg" in file:
                imglist.append(file)
        #print (imglist)
        im = imglist[0]
        #print (im)
       # with self.canvas:
        #    self.rect = Rectangle(source=im, pos =self.pos, size = self.size)
        self.Imglist()
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

    def Imglist(self):
        directory = os.listdir(self.folder.text)
        imglist = []
        for file in directory:
            if ".JPG" in file or ".jpg" in file:
                imglist.append(file)
        self.imglist = bidirectional_iterator(imglist)

    def Canvas(self,imagename):
        files = os.listdir(self.folder.text + "/Positive")
        for file in files:
            Posname = file.split("_",3)
            #if imagename == Posname[2]:
                # print rectangle

    def next(self):
        if self.imglist == []:
            #print("returning from next")
            return
        im = self.folder.text + "/" + str(self.imglist.next())
        #print(self.folder.text + "/" + str(self.imglist.next))
        print("im object = " + str(im))
        EcoCensus.abcd = im
        #print(EcoCensus.abcd)
        self.imprint.canvas.clear()
        with self.imprint.canvas:
            Rectangle(source=EcoCensus.abcd, size=self.imprint.size, pos=self.imprint.pos)
        #print (self.ids.imprint.source + "Heres the dir")
        #self.update(self, im)
        #self.Canvas(self.imglist.next())

    def prev(self):
        if self.imglist == []:
            #print ("returning from prev")
            return
        im = self.folder.text + "/" + str(self.imglist.prev())
        #print (self.folder.text + "/" + str(self.imglist.prev))
        print ("im object = " + str(im))
        EcoCensus.abcd = im
        #print(EcoCensus.abcd)
        self.imprint.canvas.clear()
        with self.imprint.canvas:
            Rectangle(source = EcoCensus.abcd, size = self.imprint.size, pos = self.imprint.pos)
        #super.ids.imprint.canvas[Rectangle].source = im
        #EventLoop.window.abcd = im
        #self.Rectangle.source = 'example.jpg'
        #print (self.ids.imprint.source + "Heres the dir")
        #Canvas(self.imglist.prev())

#class LineRectangle(Widget):
    #pass

class EcoCensus(App):
    abcd = StringProperty('example.jpg')
    def build(self):
        #FloatLayout.add_widget(LineRectangle(self, Widget))

        return Layout()

    def callback(self):
        self.abcd = Layout.prev.im


if __name__ == '__main__':
    EcoCensus().run()