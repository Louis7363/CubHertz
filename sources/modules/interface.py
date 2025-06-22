# Projet : CubHertz
# Auteurs : Louis Colbert, Luc Vallet

from modules import enregistrement_audio
import time
import customtkinter as ctk
from customtkinter import filedialog
import os
import threading


class Interface :
    def __init__(self, title, geometry):
        self.app = ctk.CTk()
        self.title = title

        self.geometry = geometry

        label = ctk.CTkLabel(self.app, text= "Bienvenue sur OeuvreVisuelVocal")
        label.grid(row = 0, column = 0, padx=(0,0), pady=(30,0))

        self.button = ctk.CTkButton(self.app, text="commencer l'enregistrement", command=self.commencer_enregistrement_interface)
        self.button.grid(row=1, column=0, padx=(0,0), pady=(20,0))

        self.audio = enregistrement_audio.Audio()

    def commencer_enregistrement_interface(self) :
        t = threading.Thread(target=self.audio.commencer_enregistrement())
        t.start()
        self.audio.creer_oeuvre()
        #self.audio.commencer_enregistrement()
        self.button.configure(text="Arrêter l'enregistrement", command=self.arreter_enregistrement_interface)

    def arreter_enregistrement_interface(self):
        self.audio.arreter_enregistrement()
        time.sleep(1)
        self.app.destroy()

    def lancer_interface(self) :
        self.app.grid_columnconfigure(0,weight=1)
        self.app.title(self.title)
        self.app.geometry(self.geometry)
        self.app.mainloop()

