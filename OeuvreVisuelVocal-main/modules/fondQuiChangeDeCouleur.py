import turtle 
from turtle import Turtle
from random import random
from modules import calculFluidite, calculRGB,positionRond

class ecran:
    def __init__(self, r, g, b, signal_audio_amplitude):
        self.r = r
        self.g = g
        self.b = b
        self.t = Turtle()
        self.i=0
        self.signal_audio_amplitude = signal_audio_amplitude
        self.max_value = max(self.signal_audio_amplitude)

    #def changeColor(self, r, g, b):
    #    self.t.screen.bgcolor(r, g, b)
    
    """def dessiner_rond(self,position) :
        turtle.speed("fastest")
        turtle.reset()
        turtle.up()
        turtle.goto(0, position)
        turtle.speed("fastest")
        turtle.down()
        turtle.color("black", "red")
        turtle.begin_fill()
        turtle.circle(50)
        turtle.end_fill()"""

    def update(self) :
        max_value = self.max_value 
        if self.i < len(self.signal_audio_amplitude)-500 :
            r1, g1, b1= calculRGB.rgb(self.signal_audio_amplitude[self.i], max_value)
            r100,g100,b100 = calculRGB.rgb(self.signal_audio_amplitude[self.i+500],max_value)
            avantR,avantG,avantB = calculFluidite.RapportCouleur(r1, g1, b1, r100,g100,b100)
            print(f"on avance de {avantR,avantG,avantB}")
            #position,positionFinale = positionRond.calculPosition(self.signal_audio_amplitude[self.i],self.signal_audio_amplitude[self.i+500],self.max_value)
            #self.dessiner_rond(position)
            #rapportPosition = calculFluidite.RapportPosition(position,positionFinale)
            for z in range (len(self.signal_audio_amplitude)/500):

                pass


                #position += rapportPosition
                #self.dessiner_rond(position)
                #self.changeColor(min(round(abs(r1+avantR), 2), 1), min(round(abs(g1+avantG), 2), 1), min(round(abs(b1+avantB), 2), 1))
                #r1,g1,b1 = r1+avantR,g1+avantG,b1+avantB
            #self.dessiner_rond(positionFinale)

            self.i += 500
            print(f"on visait{r100} et on a atteint{r1}")
            print(f"on visait{g100} et on a atteint{g1}")
            print(f"on visait{b100} et on a atteint{b1}")

            self.update()
    def lancer(self):
        self.update()