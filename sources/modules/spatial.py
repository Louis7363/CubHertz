# Projet : CubHertz
# Auteurs : Louis Colbert, Luc Vallet

from ursina import *


class Cube :
    def __init__(self, position, couleur):
        self.position = position
        self.color = couleur
        print(f"La couleur est {couleur}")
        self.cube = Entity(model='cube', color=self.color, scale=1, position=self.position)

