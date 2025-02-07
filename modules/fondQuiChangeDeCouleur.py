import turtle 
from turtle import Turtle
from random import random
from modules import calculRGB,calculFluidite

class ecran:
    def __init__(self, r, g, b, signal_audio_amplitude):
        self.r = r
        self.g = g
        self.b = b
        self.t = Turtle()
        self.i=0
        self.signal_audio_amplitude = signal_audio_amplitude

    def changeColor(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b
        self.t.screen.bgcolor(self.r, self.g, self.b)

    def calculFluidite(r1, g1, b1, r10,g10,b10) :
        pass

    def update(self) :
        max_value = max(self.signal_audio_amplitude)
        if self.i <= len(self.signal_audio_amplitude) :
            r, g, b = calculRGB.rgb(self.signal_audio_amplitude[self.i], max_value)
            self.changeColor(r, g, b)
            self.i += 10
            self.t.screen.ontimer(self.update,0)
        if self.i < len(self.signal_audio_amplitude)-100 :
            r1, g1, b1= calculRGB.rgb(self.signal_audio_amplitude[self.i], max_value)
            r100,g100,b100 = calculRGB.rgb(self.signal_audio_amplitude[self.i+100],max_value)
            avantR,avantG,avantB = calculFluidite.calculFluidite(r1, g1, b1, r100,g100,b100)
            print(f"on avance de {avantR,avantG,avantB}")
            for z in range (100) :
                self.changeColor(min(round(abs(r1+avantR), 2), 1), min(round(abs(g1+avantG), 2), 1), min(round(abs(b1+avantB), 2), 1))
                r1,g1,b1 = r1+avantR,g1+avantG,b1+avantB
            self.i += 99
            print(f"on visait{r100} et on a atteint{r1}")
            self.update()
    def lancer(self):
            self.update()
            self.t.screen.mainloop()