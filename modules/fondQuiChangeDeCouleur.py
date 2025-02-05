import turtle 
from turtle import Turtle
from random import random
from modules import calculRGB

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

    def update(self) :
        max_value = max(self.signal_audio_amplitude)
        if self.i <= len(self.signal_audio_amplitude) :
            r, g, b = calculRGB.rgb(self.signal_audio_amplitude[self.i], max_value)
            self.changeColor(r, g, b)
            self.i += 10
            self.t.screen.ontimer(self.update,0)
    def lancer(self):
            self.update()
            self.t.screen.mainloop()